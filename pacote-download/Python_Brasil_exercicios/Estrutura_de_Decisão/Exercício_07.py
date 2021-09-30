'''Faça um Programa que leia três números e mostre o maior e o menor deles'''

n1 = n2 = n3 = 0
op = ''
while op in 'sim':
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite o segundo numero: '))
    n3 = int(input('Digite o terceiro numero: '))
    if n1 > n2 and n1 > n3:
        print('O numero \033[32m{}\033[m é o maior.'.format(n1))
    if n2 > n1 and n2 > n3:
        print('O numero \033[32m{}\033[m é o maior.'.format(n2))
    if n3 > n1 and n3 > n2:
        print('O numero \033[32m{}\033[m é o maior.'.format(n3))
    if n1 < n2 and n1 < n3:
        print('O numero \033[32m{}\033[m é o menor.'.format(n1))
    if n2 < n1 and n2 <n3:
        print('O numero \033[32m{}\033[m é o menor.'.format(n2))
    if n3 < n1 and n3<n2:
        print('O numero \033[32m{}\033[m é o menor.'.format(n3))
    print('')
    op = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
print('')
print('encerrado!')
