from requests import get, post


def post_to_langvar(params=None):
    print(params)
    response = post('http://api.panlex.org/v2/langvar', params=params)
    if response.status_code == 200:
        return response.json()
    response.raise_for_status()


def post_to_expr(params=None):
    print(params)
    response = post('http://api.panlex.org/v2/expr', params=params)
    if response.status_code == 200:
        return response.json()
    response.raise_for_status()


def get_random_lang():
    settings = {"sort": "random", "limit": 1}
    result = post_to_langvar(settings)
    return result.get('result', [])[0].get('uid')


if __name__ == '__main__':
    rand_lang_id = get_random_lang()
    print(rand_lang_id)

