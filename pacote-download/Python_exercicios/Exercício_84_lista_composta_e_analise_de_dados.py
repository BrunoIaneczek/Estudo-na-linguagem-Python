'''Faça um programa que leia nome e peso de várias pessoas
guardando tudo em uma lista.No final, mostre:
A) quantas pessoas foram cadastradas.
B) uma lista com as pessoas mais pesadas
C) Uma listagem com as pessoas mais leves'''

pessoas = []
dados = []
pesos = []
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso ')))
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar?[S/N] ')).strip().lower()
    while resp not in 'nNsS':
        resp = str(input('Resposta inválida,digite novamente '))
    if resp in 'Nn':
        break
individuos = 0
# ao inves da estrutura abaixo poderia se usar o "len(pessoas)", para verificar pessoas cadastradas.
for pessoa in pessoas:
    if pessoa[0]:
        individuos += 1
    if pessoa[1]:
        pesos.append(pessoa[1])
print(f'O maior peso foi de {max(pesos)} e a pessoas que tem este peso são',end=' ')
for pessoa in pessoas:
    if max(pesos) in pessoa:
        print(pessoa[0],end='  ')

print(f'\nO menor peso foi {min(pesos)} e as pessoas que tem este peso são ',end=' ')
for pessoa in pessoas:
    if min(pesos) in pessoa:
        print(pessoa[0],end='  ')
print(f'\nForam cadastradas {individuos} pessoas.')




