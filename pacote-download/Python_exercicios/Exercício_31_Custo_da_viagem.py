# Desenvolva um programa que pergunte a distência  de uma viagem em km
# e calcule o preço da passagem, cobrando R$0,50 por km pra viagens até 200km
# e R$0,45 para viagens acimas de 200km

km = float(input('Digite quantos Kms terá a viagem '))
if km <= 200:
    print('O valor cobrado por sua viagem será de R$\033[35m{:.2f}\033[m.'.format(km*0.50))
else:
    print('O valor de sua passagem será de R$\033[31m{:.2f}\033[m.'.format(km*0.45))