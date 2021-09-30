# Faça um programa que calcule o raio de um circulo, calcule e mostre sua area.
import math
print(60*'#'), print('\033[33mEste programa calcula o raio e a área de um circulo.\033[m'), print(60*'#')
diametro = float(input('Informe qual o diametro do circulo a ser analisado: '))
raio = diametro/2
area = math.pi*(raio**2)
print('O raio deste circulo é de \033[31m{:.2f}\033[m e sua area é de \033[33m{:.2f}\033[m.'.format(raio, area))