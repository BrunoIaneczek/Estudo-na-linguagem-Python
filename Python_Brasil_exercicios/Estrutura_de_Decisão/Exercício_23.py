'''Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento.
'''

resp = 's'
while resp != 'n':
    num = float(input('Digite um numero: '))
    a=round(num)
    if num == a:
        print('Este numero e inteiro!')
    else:
        print('Este numero e decimal!')
    resp = input('Deseja continuar? [S/N] ')