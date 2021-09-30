'''FAça um programa que ajude um jogador da megasena a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
para cada jogo, cadastrando tudo em uma lista composta.'''
lista = []
from random import randint
from time import sleep
print(10*'-=-','JOGOS PARA MEGA SENA',10*'-=-')
jogos = int(input('Quantos jogos você quer gerar? '))
print(10*'-=-', f'SORTEANDO {jogos} JOGOS', 10*'-=-')
for i in range(0, jogos):
    lista.append([])
    for c in range(0, 6):
        n = randint(0,60)
        if n not in lista[i]:
            lista[i].append(n)
        else:
            lista[i].append(n+1)
for e, sub in enumerate(lista):
    sub.sort()
    sleep(1)
    print(f'Jogo {e+1}: {sub}')
print(10*'-=-', 'BOA SORTE', 10*'-=-')
