# Faça um programa que leia o sexo de uma pessoa, mas so aceite os valores
# 'M' ou 'F'.Caso esteja errado peça a digitação novamente até ter um valor correto.
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Sexo inválido digite novamente: ')).strip().upper()[0]
print('O sexo \033[34m{}\033[m, foi registrado com sucesso'.format(sexo))

