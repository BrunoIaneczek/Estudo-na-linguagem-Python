# Crie um programa que leia o ano de nascimento de sete pessoas.No final, mostre quantas
# pessoas ainda não atingiram a maioridade e quantas já são maiores.
# maioridade de 21anos
n=0
x=0
from datetime import date
for c in range(1,8):
    nasc=int(input('Em que ano a {}º pessoa nasceu?  '.format(c)))
    anoatual = date.today().year
    idade = anoatual-nasc
    if idade >=21:
        n += 1
    else:
        x += 1
print('Dentre as pessoas acima \033[35m{}\033[m atingiram a maioridade e \033[34m{}\033[m ainda não atingiram a maioridade.'.format(n,x))




