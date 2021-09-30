'''FAça um programa que tenha uma função chamada ficha, que receba 2 parametros
opcionais: O nome do jogador e quantidade de gols que ele marcou
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum
dado não tenha sido informado'''


def ficha(nome='', gols=0):
    if nome:
        if gols:
            return f'O jogador {nome} marcou {gols} gols'
        else:
            return f'O jogador {nome} marcou 0 gols'
    elif gols:
        return f'O jogador desconhecido marcou {gols}'
    else:
        return f'O jogador desconhecido marcou 0 gols'


jogador = str(input('Nome do jogador: ')).strip()
ngols = str(input('Quantos gols ele marcou: '))
if ngols.isnumeric():
    ngols = int(ngols)
else:
    ngols = 0


print(ficha(jogador, ngols))
