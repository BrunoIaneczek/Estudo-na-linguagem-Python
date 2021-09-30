# Crie um programa que leia um numero qualquer pelo teclado e mostre na tela sua porção inteira.

import math
num = float(input('Digite um numero: '))
pint =math.trunc(num)
print('A parte inteira de {} é {}.'.format(num, pint))

# Outras maneiras de execução

import math
num = float(input('Digite um numero: '))
print('O valor digitado foi {} e sua porção inteira é {}.'.format(num ,math.trunc(num)))

from math import trunc
num = float(input('Digite um numero: '))
print('O valor digitado foi {} e sua porção inteira é {}.'.format(num ,trunc(num)))
