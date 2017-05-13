from asyncio.test_utils import TestCase
from datetime import datetime
from unittest.mock import patch

from githubxml.aleatorio import sortear, dias_de_vida, segundos_de_vida


class SortearTests(TestCase):
    @patch('githubxml.aleatorio.choice')
    def test_sucesso(self, choice_mock):
        def choice_mock_fcn(lista):
            return lista[0]

        choice_mock.side_effect = choice_mock_fcn
        lista = [0, 1]
        resultado = sortear(lista)
        choice_mock.assert_called_once_with(lista)
        self.assertEqual(0, resultado)


class DataHoraTests(TestCase):
    @patch('githubxml.aleatorio.agora')
    def test_dias_de_vida(self,now_mock):
        now_mock.return_value= datetime(2015, 7, 26)
        self.assertEqual(0, dias_de_vida('26/07/2015'))
        self.assertEqual(1, dias_de_vida('25/07/2015'))

    @patch('githubxml.aleatorio.agora')
    def test_segundos_de_vida(self, now_mock):
        now_mock.return_value= datetime(2015, 7, 26)
        self.assertEqual(0, segundos_de_vida('26/07/2015'))
        self.assertEqual(60*60*24, segundos_de_vida('25/07/2015'))
