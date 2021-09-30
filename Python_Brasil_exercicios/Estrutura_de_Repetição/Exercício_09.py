'''Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50'''
for c in range(0, 50):
    a = c%2
    if a != 0:
        print(c,end=' ')
print('Fim')