# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/kh, mostre uma mensagem dizendo  que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.

from random import randint
velocidade = float(input('Informe a velocidade que você trafegava, e não minta! '))
print('Muito bem falou a verdade, a velocidade detectada pelo radar foi de {}km/h.'.format(velocidade))
if velocidade >80:
    print('Você estava acima do limite de 80km/h, você foi multado em {:.2f}R$.'.format((velocidade-80)*7))
else:
    print('Siga em frente')
print('E tenha um bom dia.')