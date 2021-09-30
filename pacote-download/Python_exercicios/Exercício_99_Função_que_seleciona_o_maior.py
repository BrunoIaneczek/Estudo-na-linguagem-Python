'''Crie um programa que tenha uma função
chamada maior(), que receba vários parâmetros com valores inteiros
seu programa tem que analisar todos os valores e dizr qual deles é maior'''
from time import sleep
'''def maior(*valores):
    tam = len(valores)
    print('Analisando os valores passados...')
    for valor in valores:
        print(f'{valor}',end=' ')
        sleep(0.4)
    print()
    print(f'Foram informados {tam} valores e o maior valor entre eles é {max(valores)}.')
    print()

maior(4,56,7,3,4,5,2,2,6,66)
maior() #Deste modo há erro na execução vazia'''

def maior(*valores):
    cont = maior = 0
    for valor in valores:
        print(f'{valor}',end=' ')
        sleep(0.4)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'O maior valor é {maior}.')
    print(f'Foram digitados {cont} valores.')

maior(3,4,5,2)
maior(3,2,4,1,4,5,6)
maior()
