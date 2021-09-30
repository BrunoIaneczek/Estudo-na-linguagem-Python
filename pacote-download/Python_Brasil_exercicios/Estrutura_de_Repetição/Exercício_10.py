'''Faça um programa que recebadois números inteiros e gere os números inteiros
que estão no intervalo compreendido por eles.'''

num1 = int(input('Digite o primeiro numero do intervalo: '))
num2 = int(input('Digite o segundo o numero do intervalo: '))
for c in range(num1+1, num2):
    print(c, end=' ')