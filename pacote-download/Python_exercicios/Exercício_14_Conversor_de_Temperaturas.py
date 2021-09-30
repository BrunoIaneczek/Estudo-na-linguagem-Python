# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

graus = float(input('Digite a temperatura em graus celsius ºC'))
fare = graus*1.8+32
print('A temperatura de ºC{:.2f} corresponde a ºF{:.2f}.'.format(graus, fare))
