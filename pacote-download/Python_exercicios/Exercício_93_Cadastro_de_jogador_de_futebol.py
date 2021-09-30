'''Crie um programa que gerencie o aproveitamento
de um jogador de futebol. O programa vai ler o nome do
 jogador e quantas partidas ele jogou. Depois vai ler
 a quantidade de gols feitos em cada partida.No final,
 tudo isso será guardado em um dicionário, incluindo o total
 de gols feitos durante o campeonato.
 '''
s=0
listagols = []
aproveitamento = {}
aproveitamento['Jogador'] = str(input('Nome do jogador: '))
aproveitamento['Partidas'] = int(input('Quantas partidas jogadas? '))
for c in range(1,aproveitamento['Partidas']+1):
    gols = int(input(f'Quantos gols fez na {c} partida? '))
    listagols.append(gols)
    s = gols+s
aproveitamento['Gols'] = listagols
aproveitamento['Total'] = s
print(30*'-=-')
print(aproveitamento)
print(30*'-=-')
for k , v in aproveitamento.items():
    print(f'O campo {k} tem valor {v}')
print()
print(f'O jogador {aproveitamento["Jogador"]} jogou {aproveitamento["Partidas"]} partidas.')
for p, g in enumerate(listagols):
    print(f'    => Na partida {p+1} ele fez {g} gols.')
print(f'Foi um total de {aproveitamento["Total"]} gols.')