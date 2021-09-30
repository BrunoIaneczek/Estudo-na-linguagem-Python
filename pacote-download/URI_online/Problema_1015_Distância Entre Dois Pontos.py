'''from math import sqrt
variaveis_float = []
x1, y1 = input('x1 y1: ').split()
x2, y2 = input('x2 y2: ').split()
variaveis = [x1, x2, y1, y2]
for var in variaveis:
    variaveis_float.append(float(var))
distancia = sqrt((variaveis_float[1]-variaveis_float[0])**2 + (variaveis_float[3]-variaveis_float[2])**2)
print(f'{distancia:.4f}')'''
'''from math import sqrt
x1 = 1.0
y1 = 7.0
x2 = 5.0
y2 = 9.0
distancia = sqrt((x2-x1)**2 + (y2-y1)**2)
print(f'{distancia:.4f}')'''

import math

linha1 = input().split(" ")
linha2 = input().split(" ")

x1,y1 = linha1
x2,y2 = linha2

distancia = math.sqrt(((float(x2) - float(x1))*(float(x2) - float(x1))) + ((float(y2)-float(y1)) *(float(y2)-float(y1))))
print(f'{distancia:.4f}')