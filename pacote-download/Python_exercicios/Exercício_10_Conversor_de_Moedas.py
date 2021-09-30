# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#considere US$1.00 = R$3.27

real = float(input('Qaunto dinheiro você tem na carteira? R$'))
dola = 3.27
print('Com R${} você pode comprar US${:.2f}'.format(real, real/dola))
