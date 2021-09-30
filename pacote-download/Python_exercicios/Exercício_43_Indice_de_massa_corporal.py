# Desenvolva um programa que leia o peso de uma pessoa, e calcule seu IMC
# e mostre seus status conforme abaixo
# Abaixo de 18.5, abaixo do peso
# Entre 18.5 e 25, peso ideal
# 25 até 30, sobrepeso
# de 30 á 40, obesidade
# acima de 40, obesidade mórbida

peso = float(input('Digite seu peso '))
altura = float(input('Digite sua altura '))
imc = peso/(altura*altura)
if imc < 18.5:
    print('Seu imc é de \033[34m{:.1f}\033[m, e você está abaixo do peso.'.format(imc))
elif imc<=25:
    print('Seu imc é de \033[34m{:.1f}\033[m, e você está no peso ideal.'.format(imc))
elif imc<=30:
    print('Seu imc é de \033[34m{:.1f}\033[m, e você tem um sobrepeso.'.format(imc))
elif imc<=40:
    print('Seu imc é de \033[31m{:.1f}\033[m, CUIDADO!! você está com obesidade. '.format(imc))
else:
    print('Seu imc é de \033[31m{:.1f}\033[m, PERIGO!! VOCÊ ESTÁ COM OBESIDADE MORBIDA.'.format(imc))
