from requests import post

PANLEX_ISO_639_LANGVARS = 7257
DISPLAY_LANGUAGE = 'eng-000'


def post_to_langvar(params=None):
    response = post('http://api.panlex.org/v2/langvar', params=params)
    if response.status_code == 200:
        return response.json()
    response.raise_for_status()


def post_to_expr(params=None):
    response = post('http://api.panlex.org/v2/expr', params=params)
    if response.status_code == 200:
        return response.json()
    response.raise_for_status()


def get_random_lang():
    settings = {"sort": "random", "limit": 1}
    result = post_to_langvar(settings)
    return result.get('result', [])[0]


def get_lang_translations(source_lang, lang_uid):
    params = {
        'trans_langvar': PANLEX_ISO_639_LANGVARS,
        'include': ['trans_txt', 'uid'],
        'uid': source_lang,
        'trans_txt':lang_uid
    }
    return post_to_expr(params)


def name_from_json(records):
    result = records['result']
    if len(result) > 0:
        return records['result'][0].get('txt', '')
    return None


def show_name(panlex_id, auto_nym, lang_name):
    print(f'Language: {auto_nym} [{panlex_id}]')
    print(f'English Name: {lang_name or "?"}')


if __name__ == '__main__':
    rand_lang = get_random_lang()
    panlex_id = rand_lang.get('uid')
    auto_nym = rand_lang.get('name_expr_txt', 'UNKNWON')
    lang_result = get_lang_translations(DISPLAY_LANGUAGE, rand_lang.get('uid', ''))
    lang_name = name_from_json(lang_result)
    show_name(panlex_id, auto_nym, lang_name)
