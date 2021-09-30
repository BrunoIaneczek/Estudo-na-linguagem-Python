'''Faça um Programa que leia três números e mostre o maior deles '''
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite segundo numero: '))
n3 = int(input('Digite terceiro numero: '))

if n1 > n2 and n1 > n3:
    print('O numero \033[36m{}\033[m é o maior.'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O numero \033[31m{}\033[m é o maior.'.format(n2))
else:
    print('O numero \033[34m{}\033[m é o maior.'.format(n3))
