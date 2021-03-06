"""
Exibe os caracteres de codigo 32 a 255 suportados pelo terminal
"""

# Python >= 2.6 compatibility
from __future__ import print_function

import sys

py_ver = sys.version_info[0]
if py_ver >= 3:
    unichr = chr

def int2byte(i):
    return bytes([i]) if py_ver >= 3 else chr(i)

cod_saida = sys.stdout.encoding

if cod_saida.upper().startswith('UTF'):
    print('Terminal %s, exibindo caracteres Unicode U+0020 a U+00FF' % cod_saida)
    cars_uni = [unichr(i) for i in range(0x20, 0x100)]
else:
    print('Terminal %s, exibindo caracteres 0x20 a 0xff' % cod_saida)
    cars_uni = [int2byte(i).decode(cod_saida) for i in range(0x20, 0x100)]

for i, car in enumerate(cars_uni):
    print(car, end=' ')
    if i % 32 == 31:
        print()
