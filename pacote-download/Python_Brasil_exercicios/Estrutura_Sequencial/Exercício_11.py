# Faça um programa que peça dois numeros inteiros e um numero real:
# Mostre o produto do dobro do primeiro com metade do segundo, a soma do triplo do primeiro com o terceiro e o terceiro elevado ao cubo
print('\033[34mCalculador dinâmico\033[m')
n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite um segundo numero inteiro: '))
n3 = float(input('Digite um numero real qualquer: '))
a = (2*n1)*(n2/2)
b = (3*n1)+n3
c = n3**3
print('O produto do dobro do primeiro com metade do segundo é \033[33m{:.2f}\033[m.'.format(a))
print('A soma do triplo do primeiro com o terceiro é \033[34m{:.2f}\033[m.'.format(b))
print('O valor do terceiro elevado ao cubo é \033[32m{:.2f}\033[m.'.format(c))