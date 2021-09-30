# Faça um programa que leia um comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math
cp = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
#hipo = (math.pow(cp,2))+(math.pow(ca,2))
#print('Em triângulo onde seu cateto oposto é {} e seu cateto adjacente é {} o comprimento da sua hipotenusa é {:.2f}'
#      .format(cp ,ca , math.sqrt(hipo)))

# outra maneira
hi = math.hypot(cp ,ca)
print('A hipotenusa é {:.2f}'.format(hi))