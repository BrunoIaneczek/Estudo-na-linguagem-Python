# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Digite um ano qualquer '))
a = ano % 4
b = ano % 400
c = ano % 100
if a == 0 and c != 0 or b == 0:
    print('O ano de \033[32m{}\033[m é bissexto.'.format(ano))
else:
    print('O ano de \033[36m{}\033[m não é bissexto'.format(ano))



