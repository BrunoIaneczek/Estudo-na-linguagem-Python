
'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.'''

resp = 'Ss'
while resp not in 'Nn':
    num1 = float(input('Digite o primeiro número: '))
    if num1 % 2 == 0:
        print('O numero acima e par.')
    else:
        print('O numero acima é ímpar.')
    if num1 > 0:
        print('O numero acima e positivo.')
    else:
        print('O numero acima é negativo.')
    a = round(num1)
    if a == num1:
        print('O numero acima é inteiro.')
    else:
        print('O numero acima é decimal.')
    num2 = float(input('Digite o segundo número: '))
    b = round(num2)
    if num2 % 2 == 0:
        print('O número acima é par.')
    else:
        print('O número acima é ímpar.')
    if num2 > 0:
        print('O número acima é positivo.')
    else:
        print('O número acima é negativo')
    if num2 == b:
        print('O número acima é inteiro.')
    else:
        print('O número acima é decimal.')
    resp = str(input('Deseja continuar [S/N]? '))
    while resp not in 'SsNn':
        resp = str(input('Resposta inválida, digite [S/N]: '))
