# Faça um programa que converta temperaturas em farenheit em graus celsios.
print(60*'\033[34m==\033[m'), print('\033[31mConversor de temperatura farenheit/celcius.\033[m'), print(60*'\033[34m==\033[m')
temp = float(input('Digite a temperatura a ser convertida: '))
celsius = 5*((temp-32)/9)
print('A temperatura em graus celsius e de \033[31m{:.2f}º\033[m.'.format(celsius))