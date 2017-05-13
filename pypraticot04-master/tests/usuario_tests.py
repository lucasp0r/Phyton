from asyncio.test_utils import TestCase
import json
from unittest.mock import patch, Mock

from githubxml import usuario

dct = {'following_url': 'https://api.github.com/users/renzon/following{/other_user}', 'hireable': False,
       'avatar_url': 'https://avatars.githubusercontent.com/u/3457115?v=3', 'blog': 'https://adm.python.pro.br',
       'company': 'Python Pro', 'name': 'Renzo Nuccitelli', 'bio': None, 'id': 3457115,
       'gists_url': 'https://api.github.com/users/renzon/gists{/gist_id}',
       'starred_url': 'https://api.github.com/users/renzon/starred{/owner}{/repo}', 'location': 'Brazil',
       'gravatar_id': '', 'html_url': 'https://github.com/renzon', 'login': 'renzon',
       'events_url': 'https://api.github.com/users/renzon/events{/privacy}', 'email': 'renzo@python.pro.br',
       'followers': 171, 'created_at': '2013-02-02T14:15:53Z', 'url': 'https://api.github.com/users/renzon',
       'public_gists': 11, 'received_events_url': 'https://api.github.com/users/renzon/received_events',
       'site_admin': False, 'public_repos': 63,
       'subscriptions_url': 'https://api.github.com/users/renzon/subscriptions',
       'followers_url': 'https://api.github.com/users/renzon/followers', 'following': 3,
       'updated_at': '2015-07-13T18:54:03Z', 'type': 'User',
       'organizations_url': 'https://api.github.com/users/renzon/orgs',
       'repos_url': 'https://api.github.com/users/renzon/repos'}


class AcessarDadosTests(TestCase):
    @patch('githubxml.usuario.requests')
    def test_sucess(self, requests_mock):
        js = json.dumps(dct)
        response = Mock()
        response.content = js.encode('utf8')
        get_mock = Mock(return_value=response)
        requests_mock.get = get_mock
        resultado = usuario.acessar_dados('renzon')
        get_mock.assert_called_once_with('https://api.github.com/users/renzon')
        self.assertDictEqual(dct, resultado)
