'''Crie um programa que simule o funcionamento
de um caixa eletrônico.No inicio, pergunte ao usuário qual será
o valor a ser sacado (numero inteiro) e o programa vai
informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50,R$20,R$10 e R$1.'''
print('{:-^40}'.format('Banco BRU'))
while True:
    saque = int(input('Qual o valor deseja sacar? R$'))
    n50 = saque//50
    if n50 != 0:
        print(f'Total de {n50} cédulas de R$50.')
    a = saque-(n50*50)
    n20 = a//20
    if n20 != 0:
        print(f'Total de {n20} cédulas de R$20.')
    b = a-(n20*20)
    n10 = b//10
    if n10 != 0:
        print(f'Total de {n10} cédulas de R$10.')
    c = b-(n10*10)
    n1= c//1
    if n1 != 0:
        print(f'Total de {n1} cédulas de R$1.')

    break
#print(f'Total de {n50} cédulas de R$50.')
#print(f'Total de {n20} cédulas de R$20.')
#print(f'Total de {n10} cédulas de R$10.')
#print(f'Total de {n1} cédulas de R$1.')
print('{:-^40}'.format('FIM DO SAQUE'))