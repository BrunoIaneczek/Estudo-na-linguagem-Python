'''Faça um programa que jogue par ou impar com o computador.
O jogo será interrompido quando o jogador perde mostrando o total de vitorias consecutias
que ele conquisto no fim do jogo'''
from random import  randint
c=0
while True:
    print(30*'-')
    n = int(input('Digite um valor: '))
    escolha = str(input('Você escolhe par ou impar [P/I]? ')).strip().lower()[0]
    pcn = randint(0,10)
    spu = n+pcn
    div = spu%2
    a = 'voce perdeu'
    b = 'voce ganhou'
    print(30*'-')
    if div == 0 and escolha == 'p':
        print(f'Você jogou {n} e o computador jogou {pcn} que somados é {n+pcn} que é par,{b}')
        c+=1
    if div == 1 and escolha == 'i':
        print(f'Você jogou {n} e o computador jogou {pcn} que somados são {n+pcn} que é impar,{b}')
        c+=1
    if div == 0 and escolha == 'i':
        print(f'Você jogou {n} e o computador jogou {pcn} que somados é {n+pcn} que é par,{a}')
        break
    if div == 1 and escolha == 'p':
        print(f'Você jogou {n} e o computador jogou {pcn} que somados é {n+pcn} que é impar,{a}')
        break
    print('vamos jogar novamente')
print(30*'-')
print('Você perdeu!!')
print(f'Você ganhou {c} vezes.')
