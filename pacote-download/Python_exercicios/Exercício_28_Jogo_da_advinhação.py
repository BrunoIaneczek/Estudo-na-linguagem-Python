# Escreva um programa que faça o computador "pensar" em numero inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador.

from time import sleep
from random import randint
print('Vou pensar em numero tente advinhar...')
pc = randint(0, 5)
usuario = int(input('Digite o número que acha que eu pensei '))
print('processando...')
sleep(3)
if pc == usuario:
    print('Parabens vc acertou!')
else:
    print('kkkkkkkkkk, o número que pensei foi {} e não {}, eu venci'.format(pc, usuario))
