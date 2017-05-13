from datetime import date
import datetime
from random import choice, shuffle, sample


def sortear(lista):
    return choice(lista)

def dias_de_vida(nascimento='02/09/1982'):
    return round(segundos_de_vida(nascimento)/(3600*24))


def segundos_de_vida(nascimento):
    datahora_nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')
    datahora = agora()
    time_delta = datahora - datahora_nascimento
    return time_delta.total_seconds()


def agora():
    return datetime.datetime.now()


if __name__ == '__main__':
    lista = list(range(10))
    print(sortear(lista))
    shuffle(lista)
    print(lista)
    print(sample(lista, 2))
    print(''.join(sample('Renzo',2)))
