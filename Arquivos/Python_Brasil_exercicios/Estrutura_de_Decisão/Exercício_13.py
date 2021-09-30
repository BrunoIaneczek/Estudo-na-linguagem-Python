'''Faça um Programa que leia um número e exiba o dia correspondente da semana
. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''

resp = ''
while resp != 0:
    resp = int(input('Digite um numero para saber o dia da semana: '))
    if resp == 1:
        print('O dia é domingo.')
    if resp == 2:
        print('O dia é segunda-feira')
    if resp == 3:
        print('O dia e terça-feira.')
    if resp == 4:
        print('O dia é quarta-feira.')
    if resp == 5:
        print('O dia é quinta-feira.')
    if resp == 6:
        print('O dia é sexta-feira.')
    if resp == 7:
        print('O dia é sábado.')
print('Fim do programa.')