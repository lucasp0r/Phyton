class Operacao():
    def calcular(self, param, param1):
        raise NotImplementedError()


class Adicao(Operacao):
    def calcular(self, param, param1):
        return param + param1


class Diferenca(Operacao):
    def calcular(self, param, param1):
        return param - param1


class Calculadora():
    def __init__(self):
        self._param1 = None
        self._param = None
        self._sinal = None
        self._operacoes = {}

    def adicionar_operacao(self, sinal, operacao):
        self._operacoes[sinal] = operacao

    def operacao(self, sinal):
        return self._operacoes[sinal]

    def efetuar_operacao(self, sinal, param, param1):
        operacao = self._operacoes[sinal]
        return operacao.calcular(param, param1)

    def obter_inputs_e_efetuar_operacao(self):
        self._obter_inputs()
        return self.efetuar_operacao(self._sinal, self._param, self._param1)

    def _obter_inputs(self):
        self._param = float(meu_input('Digite o primeiro número: '))
        self._sinal = meu_input('Digite o sinal da operação: ')
        self._param1 = float(meu_input('Digite o segundo número: '))

class CalculadoraPrefixa(Calculadora):
    def _obter_inputs(self):
        self._sinal = meu_input('Digite o sinal da operação: ')
        self._param = float(meu_input('Digite o primeiro número: '))
        self._param1 = float(meu_input('Digite o segundo número: '))

def meu_input(msg):
    return input(msg)

if __name__=='__main__':
    calculadora=CalculadoraPrefixa()
    calculadora.adicionar_operacao('+', Adicao())
    print(calculadora.obter_inputs_e_efetuar_operacao())
