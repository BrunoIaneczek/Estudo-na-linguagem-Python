# Faça um programa que peça a temperatura em graus celsius e converta para farenheit.
print(60*'\033[31m-\033[m'), print('\033[34mConversor de graus celsius em farenheit.\033[m'), print(60*'\033[31m-\033[m')
graus = float(input('Digite sua temperatura em graus celsius: '))
f = (graus*9/5)+32
print('A temperatura em farenheit é de \033[34m{:.2f}\033[m.'.format(f))
