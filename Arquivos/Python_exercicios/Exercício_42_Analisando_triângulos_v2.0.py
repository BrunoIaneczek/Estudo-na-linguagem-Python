#Refaça o exercicio 35 e acrescente se ele é equilatero, isóceles ou escaleno:

r1 = float(input('Primeiro segmento '))
r2 = float(input('Segundo segmento '))
r3 = float(input('Terceirro segmento '))
if r1 < r2+r3 and r2<r1+r3 and r3<r2+r1:
    print('Os segmentos acima podem formar um triângulo')
    if r1 == r2 == r3:
        print('O triãngulo formado é equilátero')
    elif r1 == r2 != r3 or r2==r3 !=r1 or r1==r3 !=r2:
        print('O triângulo é isóceles')
    elif r1 != r2 != r3 != r1:
        print('O triãngulo é escaleno')
else:
    print('Os segmentos acima nao podem formar um triângulo')
