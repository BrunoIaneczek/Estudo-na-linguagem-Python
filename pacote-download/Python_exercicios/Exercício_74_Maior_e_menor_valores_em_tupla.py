'''Crie um programa que vai gerar cinco números aleatórios
e colocar em uma tupla. Depois disso, mostre a listagem de números
gerados e também indique o menor e maior valor na tupla'''

from random import randint

a = randint(0,10)
b = randint(0,10)
c = randint(0,10)
d = randint(0,10)
e = randint(0,10)
numeros = a, b, c, d, e
#METODO CURSO EM VIDEO
#elementos = ((randint(0,10)),(randint(0,10)),(randint(0,10)),(randint(0,10)),(randint(0,10)),(randint(0,10)))
#print(elementos)
print(f'Alistagem de numeros é {numeros}.')
print(f'O maior numero da listagem é {max(numeros)}.')
print(f'O menor número da listagem é {min(numeros)}.')
