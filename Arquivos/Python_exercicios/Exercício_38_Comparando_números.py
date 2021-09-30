# Escreva um programa que leia dois números inteiros e compare-os mostrando na tela:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais.

v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
if v1 > v2:
    print('O primeiro valor \033[31m{}\033[m é maior que o segundo valor \033[32m{}\033[m.'.format(v1,v2))
elif v1 == v2:
    print('Os dois valores são \033[31miguais\033[m.')
else:
    print('O segundo valor \033[34m{}\033[m é maior que o primeiro valor \033[33m{}\033[m.'.format(v2,v1))
