'''Faça um programa que leia 5 números e informe a soma e a média dos números.'''
numeros = []
s = 0
for c in range(0, 5):
    num = int(input('Digite um numero: '))
    numeros.append(num)
    s+=num
media = s/5
print(f'A soma entre os números digitados é \033[35m{s}\033[m é a media entre eles é \033[34m{media:.2f}\033[m.')