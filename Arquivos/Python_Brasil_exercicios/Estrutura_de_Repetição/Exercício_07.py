'''Faça um programa que leia 5 números e informe o maior número.'''
numeros = []
for c in range(0, 5):
    num = int(input('Digite um numero: '))
    numeros.append(num)
print(f'O maior entre os numeros digitados é \033[34m{max(numeros)}\033[m.')
