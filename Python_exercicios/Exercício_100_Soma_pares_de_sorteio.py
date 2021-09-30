'''Faça um programa que tenha uma lista chamada números
e duas funções chmadas de sortei e somapar
A primeira função vai sorteae 5 números e vai coloca-los em uma lista
e a segunda vai somar todos os valores pares na lista'''

from random import randint

numeros = []
pares = []


def sortei():
    for c in range(0, 10):
        n = randint(0, 10)
        numeros.append(n)
    print('Os numeros na lista são: ', end='')
    for i in numeros:
        print(f'\033[31m{i}\033[m', end=' ')
    print()


def somapar():
    s = 0
    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
    print('Os valores pares na lista são', end=' => ')
    for v in pares:
        s += v
        print(f'\033[34m{v}\033[m', end=' ')
    print(f'e a soma entre eles é {s}.')


sortei()
somapar()
# função sem parametros nao totalmente errado mas não exato