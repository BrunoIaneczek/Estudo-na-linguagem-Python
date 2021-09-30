# Faça um programa que converta metros em centimetros

print(25*'=='),print('\033[35mEste programa converte centimetros para metros.\033[m'),print(25*'==')
medida = float(input('Digite a medida em centimetros: '))
metros = medida/100
print('A medida em metros é de \033[34m{:.2f}m\033[m.'.format(metros))