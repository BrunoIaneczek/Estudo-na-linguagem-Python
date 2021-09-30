# Escreva um programa que que leia um valor em metros e o exiba convertido em centimetro e milimetros.

dist = float(input('Digite uma distancia em metros:  '))
cent = dist*100
mil = dist*1000
print('A distância de {}m em centimetros é de {}cm e em milimetros é em {}mm'.format(dist, cent, mil))