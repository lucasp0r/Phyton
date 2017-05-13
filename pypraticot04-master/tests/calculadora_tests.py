from asyncio.test_utils import TestCase
from unittest.mock import Mock, patch

from githubxml.calculadora import Adicao, Operacao, Diferenca, Calculadora


class OperacaoTests(TestCase):
    def test_raise_not_implement(self):
        operacao = Operacao()
        self.assertRaises(NotImplementedError, operacao.calcular, 1, 1)


class SomaTests(TestCase):
    def test_calcular(self):
        operacao = Adicao()
        self.assertIsInstance(operacao, Operacao)
        self.assertEqual(2, operacao.calcular(1, 1))
        self.assertEqual(2.3, operacao.calcular(1.1, 1.2))


class DiferencaTests(TestCase):
    def test_calcular(self):
        operacao = Diferenca()
        self.assertIsInstance(operacao, Operacao)
        self.assertEqual(0, operacao.calcular(1, 1))
        self.assertAlmostEqual(-0.1, operacao.calcular(1.1, 1.2), places=12)


class CalculadoraTests(TestCase):
    def test_adicionar_operacao(self):
        calculadora = Calculadora()
        adicao = Adicao()
        calculadora.adicionar_operacao('+', adicao)
        self.assertIs(adicao, calculadora.operacao('+'))

    def test_efetuar_operacao(self):
        calculadora = Calculadora()
        operacao = Mock()
        operacao.calcular = Mock(return_value=3)
        calculadora.adicionar_operacao('-', operacao)
        self.assertIs(3, calculadora.efetuar_operacao('-', 1, 3))
        operacao.calcular.assert_called_once_with(1, 3)


    @patch('githubxml.calculadora.meu_input')
    def test_efetuar_operacao(self, input_mock):
        calculadora = Calculadora()
        index_call=-1

        def returnar_inputs(msg):
            nonlocal index_call
            index_call +=1
            return [1, '-' , 3][index_call]

        input_mock.side_effect=returnar_inputs
        operacao = Mock()
        operacao.calcular = Mock(return_value=3)
        calculadora.adicionar_operacao('-', operacao)
        self.assertIs(3, calculadora.obter_inputs_e_efetuar_operacao())
        operacao.calcular.assert_called_once_with(1, 3)
