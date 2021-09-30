'''Aprimore o desafio 93 para que ele funcione
com vários jogadores, incluindo um sistema de visualização
de detalhes do aproveitamento de cada jogador'''
listajogadores = []
listagols = []
aproveitamento = {}
while True:
    aproveitamento['Jogador'] = str(input('Nome do jogador: '))
    partidas = int(input('Quantas partidas jogadas? '))
    for c in range(1,partidas+1):
        gols = int(input(f'Quantos gols fez na {c} partida? '))
        listagols.append(gols)
    aproveitamento['Gols'] = listagols[:]
    aproveitamento['Total'] = sum(listagols)
    listagols.clear()
    resp = str(input('Quer continuar? '))[0]
    while resp not in 'SsNn':
        resp = str(input('Digite [S/N]: '))[0]
    listajogadores.append(aproveitamento.copy())
    if resp in 'Nn':
        break
print(30*'=-=')
for t in aproveitamento.keys():
    print(f'{t:<15}',end='')
print()
for k,v in enumerate(listajogadores):
    print(f'{k:>2}',end=' ')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print(30*'-=-')
#print(aproveitamento)
#print(listajogadores)
print(30*'-=-')
listaatletas = []
for i ,c in enumerate(listajogadores):
    listaatletas.append(i)
while True:
    atleta = int(input('Qual jogador deseja ver o rendimento? '))
    while atleta not in listaatletas and atleta != 999:
        atleta = int(input('Jogador não está na lista, digite um cód válido:  '))
    print(30*'-=-')
    if atleta != 999:
        print(f'Levantamento do jogador {listajogadores[atleta]["Jogador"]}')
        for p, g in enumerate(listajogadores[atleta]["Gols"]):
                    print(f'    => Na partida {p+1} ele fez {g} gols.')
        print(f'    =>O total de gols  foi \033[34m{listajogadores[atleta]["Total"]}\033[m')
    else:
        print('PROGRAMA ENCERRADO')
        break

