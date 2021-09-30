'''Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo'''

opcao = ''
while opcao in 'Ss':
    n1 = int(input('Digite um numero: '))
    if n1 < 0:
        print('O numero e negativo.')
    elif n1 == 0:
        print('O valor é nulo.')
    else:
        print('O valor é positivo')
    opcao = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
print('encerrado')