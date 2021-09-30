"""Crie um programa que leia nome,ano de nascimento e carteira
de trabalho e cadastre-os(com idade) em um dicionário
se por acaso a CTPS for diferente de 0 o dicionário
receberá também o ano de contratação e o salário. Calcule
e acrescente além da idade, com quantos anos a pessoa vai se aposentar
"""
from datetime import date
anoatual = date.today().year
trabalhador = {'Nome': str(input('Nome do trabalhador: ')), 'Ano de nascimento': int(input('Ano de nascimento: ')),
               'Numero da CTPS': int(input('Numero da CTPS: '))}
trabalhador['Idade'] = anoatual-trabalhador['Ano de nascimento']
if trabalhador['Numero da CTPS'] != 0:
    trabalhador['Salário'] = float(input('Digite o valor salário: R$'))
    trabalhador['Ano de contração'] = int(input('Ano de contratação: '))
    trabalhador['Idade para se aposentar'] = (trabalhador['Ano de contração'] - trabalhador['Ano de nascimento'])+35
print(30*'-=-')
for k, v in trabalhador.items():
    print(f'{k} é {v}.')
