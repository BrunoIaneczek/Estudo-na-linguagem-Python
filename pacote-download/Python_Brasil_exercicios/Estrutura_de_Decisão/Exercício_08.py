'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.'''

p1 = p2 = p3 = 0
op = ''
while op in 'sim':
    p1 = float(input('Qual é o valor do primeiro produto? '))
    p2 = float(input('Qual é o valor do segudo produto? '))
    p3 = float(input('Qual é o valor do terceiro produto? '))
    if p1 < p2 and p1 < p3:
        print('Você deve comprar o primeiro produto')
    if p2 < p1 and p2 < p3:
        print('Você deve comprar o  segundo produto ')
    if p3 < p1 and p3 < p2:
        print('Você deve comprar o terceiro produto')
    op = str(input('Deseja verificar novamente? [S/N] '))
print('')
print('Encerrado')

