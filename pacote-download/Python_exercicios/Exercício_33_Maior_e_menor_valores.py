# Faça um programa que leia três numeros e mostre qual é o maior e qual o menor.

n1 = int(input('Digite o primeiro número '))
n2 = int(input('Digite o segundo número '))
n3 = int(input('Digite o terceiro número '))
if n1<n2 and n1<n3 and n2>n3:
    print('O maior número é \033[34m{}\033[m.'.format(n2))
    print('E o menor número é \033[31m{}\033[m.'.format(n1))
if n1<n2 and n1<n3 and n3>n2:
    print('O maior número é \033[36m{}\033[m.'.format(n3))
    print('E o menor número é \033[35m{}\033[m.'.format(n1))
if n2<n1 and n2<n3 and n1>n3:
    print('O maior número é \033[31m{}\033[m.'.format(n1))
    print('E o menor número é \033[33m{}\033[m.'.format(n2))
if n2<n1 and n2<n3 and n3>n1:
    print('O maior numero é \033[34m{}\033[m.'.format(n3))
    print('E o menor número é \033[35m{}\033[m.'.format(n2))
if n3<n1 and n3<n2 and n1>n2:
    print('O maior número é \033[36m{}\033[m.'.format(n1))
    print('E o menor núemro é \033[33m{}\033[m.'.format(n3))
if n3<n1 and n3<n2 and n2>n1:
    print('O maior número é \033[34m{}\033[m.'.format(n2))
    print('E o menor número é \033[31m{}\033[m.'.format(n3))