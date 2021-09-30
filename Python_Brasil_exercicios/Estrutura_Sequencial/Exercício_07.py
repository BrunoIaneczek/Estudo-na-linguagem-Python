# Faça um programa que calcule a área  de um quadrado e mostre o dobro desta área ao usuário

print(60*'\033[31m==\033[m'), print('\033[36mEste programa calcula a área de um quadrado e mostra o dobro da mesma\033[m.'), print(60*'\033[31m==\033[m')
lado = float(input('Digite a media do lado do quadrado: '))
area = lado*lado
dobroarea = area*2
print('A área do quadrado é \033[33m{:.2f}\033[m e o dobro da área é \033[33m{:.2f}\033[m.'.format(area, dobroarea))
