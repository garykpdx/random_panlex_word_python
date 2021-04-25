from requests import get, post


def post_to_langvar(data=None):
    response = get('http://api.panlex.org/v2/langvar', data=data)
    if response.status_code == 200:
        return response.json()
    response.raise_for_status()


def get_random_lang():
    data = {"sort": "random", "limit": 1}
    result = post_to_langvar(data)
    return result.get('result', [])[0].get('uid')

if __name__ == '__main__':
    rand_lang_id = get_random_lang()
    
