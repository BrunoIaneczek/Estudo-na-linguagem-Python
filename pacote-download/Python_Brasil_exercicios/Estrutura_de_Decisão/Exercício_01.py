'''Faça um Programa que peça dois números e imprima o maior deles..'''

opcao = ''
while opcao in 'Ss':
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite outro numero: '))
    if n1 > n2:
        print('O numero {} é o de maior valor.'.format(n1))
    else:
        print('O numero {} é o de maior valor.'.format(n2))
    print(' ')
    opcao = str(input('Você quer continuar [S/N]: ')).strip().upper()[0]
print('Encerrado')