# faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math
ang = float(input('Digite o valor do ângulo: '))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
sen = math.sin(math.radians(ang))
print('No ângulo {}º seu seno é de {:.2f}, seu cosseno é de {:.2f} e a sua tangente {:.2f}'.format(ang, sen, cos, tan))

