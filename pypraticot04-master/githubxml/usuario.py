import json

import requests


def acessar_dados(usuario):
    response = requests.get('https://api.github.com/users/%s' % usuario)
    decoded_json = response.content.decode('utf8')
    js = json.loads(decoded_json)
    return js


if __name__ == '__main__':
    print(acessar_dados('renzon'))
