#Faça um programa que leia o peso de 5 pessoas.No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for x in range(1,6):
    peso = float(input('Digite o peso da {}º pessoa '.format(x)))
    if x == 1:
        maior = peso
        menor = peso
    else:
        if peso >maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {}kg'.format(maior))
print('O menor peso é {}kg'.format(menor))


























