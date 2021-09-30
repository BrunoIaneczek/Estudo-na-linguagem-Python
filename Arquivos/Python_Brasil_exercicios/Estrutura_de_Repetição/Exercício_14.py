''' Faça um programa que peça 10 números inteiros,
calcule e mostre a quantidade de números pares e a quantidade de números impares. '''
numeros = []
pares = []
impares = []
tampares = 0
tamimpares = 0
for v in range(0, 10):
    numero = int(input('Digite um número: '))
    numeros.append(numero)
for valor in numeros:
    if valor % 2 == 0:
        pares.append(valor)
        tampares = len(pares)
    else:
        impares.append(valor)
        tamimpares = len(impares)
print(30*'-=')
print('Os valores pares digitados foram:')
for p in pares:
    print(f'{p}', end=' ')
print()
print(f'E foram digitados {tampares} números.')
print(20*'-=')
print('Os valores impares digitados foram: ')
for i in impares:
    print(i, end=' ')
print()
print(f'E foram digitados {tamimpares} numeros.')

lista = {}
lista['pares']= pares[:]
lista['impares'] = impares[:]
