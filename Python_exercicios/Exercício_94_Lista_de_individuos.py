'''Crie um programa que leia sexo, nome e idade de várias pessoas.
Guardando os dados de cada pessoa em um dicionário e
todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade do grupo
C) Uma lista como todas as mulheres
D) Uma lista com todas as pessoas com idade acima da média.'''
lista = []
idades = []
individuo = {}
while True:
    individuo['nome'] = str(input('Nome: '))
    individuo['idade'] = int(input('Idade: '))
    individuo['sexo'] = str(input('Sexo: '))[0]
    while individuo['sexo'] not in 'FfMm':
        individuo['sexo'] = str(input('Sexo errado digite novamente: '))[0]
    lista.append(individuo.copy())
    resp = str(input('Deseja continuar? '))[0]
    while resp not in 'SsNn':
        resp = str(input('Por favor digite novamente: '))[0]
    if resp in 'Nn':
        break
print('As mulheres do grupo são',end=' ')
for i in range(0,len(lista)):
    idades.append(lista[i]['idade'])
    if lista[i]['sexo'] in 'Ff':
        print(lista[i]['nome'],end=' ')
media = sum(idades)/len(lista)
print()
print('As pessoas acima da média são ',end=' ')
for i in range(0,len(lista)):
    if lista[i]['idade'] > media:
        print(lista[i]['nome'],end=' ')
print()
print(f'O número de pessoas na lista é {len(lista)}')
print(f'A média de idade do grupo é {media:.2f}')






