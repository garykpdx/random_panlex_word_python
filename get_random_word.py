import json

from requests import post

PANLEX_ISO_639_LANGVARS = 7257


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


if __name__ == '__main__':
    pass
