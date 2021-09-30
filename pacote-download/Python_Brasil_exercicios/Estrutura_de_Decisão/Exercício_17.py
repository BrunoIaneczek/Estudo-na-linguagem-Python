'''Faça um Programa que peça um número correspondente a um determinado ano
e em seguida informe se este ano é ou não bissexto.'''

while True:
    ano = int(input('Digite o ano, para saber se é bissexto: '))
    if ano % 4==0 and not ano % 100==0:
        print('é bissexto')
    elif ano % 100==0 and ano % 400 == 0:
        print('é bissexto')
    else:
        print('Nao é bissexto')