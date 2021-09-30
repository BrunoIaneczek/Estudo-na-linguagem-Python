'''Crie um programa onde 4 jogadores joguem um dado
e tenham resultados aleatórios.Guarde esses resultados
em um dicionário. No final, coloque esse dicionário
em ordem, sabendo que o vencedor tirou o maior número
no dado'''
from random import randint
from time import sleep
from operator import  itemgetter
resultados = {}
for c in range(1, 5):
    resultados[f'Jogador{c}'] = randint(1, 6)
ranking = ()
print('Valores sorteados')
sleep(1)
for k, v in resultados.items():
    print(f'O {k} tirou no dado {v}')
    sleep(1)
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True) # o elemento 1 entre parenteses remete ao item que qero ordenar, neste caso o valor do dado
print('Ranking dos jogadores')
for i , v in enumerate(ranking):
    print(f'O {i+1}º lugar foi do {v[0]} com {v[1]}.')
    sleep(1)




