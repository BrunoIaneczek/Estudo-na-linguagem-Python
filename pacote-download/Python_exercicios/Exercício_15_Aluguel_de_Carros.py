# Escreva um programa que pergunte a quantidade de Km precorridos por um carro alugado
#e a quantidade de dias  pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
# custa R$60 por dia e R$0.15 por km rodado.

dias = float(input('Digite  quantos dias de aluguel: '))
kms = float(input('Digite kms rodados: '))
valuguel = dias*60
vkms = kms*0.15
print('O valor total a pagar e de R${}.'.format(valuguel+vkms))