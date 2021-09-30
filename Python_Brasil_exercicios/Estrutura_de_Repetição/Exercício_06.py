'''Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
 Depois modifique o programa para que ele mostre os números um ao lado do outro.'''
def titulo(txt):
    tam = len(txt)+4
    print(tam*'=')
    print(f'  \033[34m{txt}\033[m')
    print(tam*'=')
    print()


def colunanumericavertical(inicio, fim):
    for c in range(inicio, fim+1):
        print(f'\033[31m{c}\033[m')
    print()


def colunanumericahorizontal(inicio, fim):
    for c in range(inicio, fim+1):
        print(f'\033[33m{c}\033[m',end=' ')
    print()



colunanumericavertical(1, 20)
titulo('Agora um ao lado do outro!!')
colunanumericahorizontal(1, 20)