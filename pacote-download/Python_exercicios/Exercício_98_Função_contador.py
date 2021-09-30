"""Faça um programa que tenha uma função chamada contador()
que rceba três parâmetros: inicio, fim e passo e realize
a contagem.
Seu programa tem que realizar três contagens através da
função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""
from time import sleep
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo = passo * -1
    if inicio > fim:
        passo = passo * -1
        fim = fim - 1
    else:
        passo = passo
        fim = fim + passo
    if fim > inicio:
        print(f'contando de {inicio} a {fim - passo} de {passo} em {passo}')
        for c in range(inicio, fim, passo):
            sleep(0.3)
            print(c, end=' ')
        print()
        print(20 * '-=-')

    else:
        print(f'contando de {inicio} a {fim + 1} de {passo * -1} em {passo * -1}')
        for c in range(inicio, fim, passo):
            sleep(0.3)
            print(c, end=' ')
        print()
        print(20 * '-=-')


contador(1, 10, 1)
contador(10, 0, 2)
print('Contagem personalizada')
print(20 * '=')
inicio = int(input('Digite o numero inicial: '))
fim = int(input('Digite numero final: '))
passo = int(input('Digite o passo: '))
contador(inicio, fim, passo)
