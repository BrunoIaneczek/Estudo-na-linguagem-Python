# Desenvolvaum programa que leia o comprimento  de três retas e diga ao usuário se eles podem ou não formar um triângulo

r1 = float(input('Primeiro segmento '))
r2 = float(input('Segundo segmento '))
r3 = float(input('Terceirro segmento '))
if r1 < r2+r3 and r2<r1+r3 and r3<r2+r1:
    print('Os segmentos acima podem formar um triângulo')
else:
    print('Os segmentos acima nao podem formar um triângulo')