'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento
de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas.'''
print(20*'==','\033[31mMulta por excesso de peixe\033[m',20*'==')

print('''Todo peixe pescado acima do limite de 50kg, deverá ser cobrado,
R$4,00 por kilo excedente.''')
print(50*'==')
peso = float(input('informe a quantidade de pescado: '))
if peso <= 50:
    print('A quantidade de pescado está dentro do limite.')
else:
    excedente = peso-50
    multa = excedente*4.00
    print('A quantidade de pescado excedeu o limite em \033[32m{:.3f}Kg\033[m, e deverá pagar uma multa de \033[31m{:.2f}R$.\033[m'.format(excedente,multa))