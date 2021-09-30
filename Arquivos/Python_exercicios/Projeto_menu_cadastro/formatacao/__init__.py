# Funções para títulos
def titulo1 (msg):
    print(60*'=')
    print(msg.center(60)) # Centraliza o texto
    print(60 * '=')

def titulo2 (msg):
    print(60*'\033[34m=\033[m')
    print(f'{msg:^60}')
    print(60 * '\033[34m=\033[m')

def titulo3 (msg):
    print(60*'\033[32m#\033[m')
    print(f'{msg:^60}')
    print(60 * '\033[32m#\033[m')


# Função para espaçamento
def espaco(espaco,qtdespaco):
    for n in range(0,qtdespaco):
        print(espaco)


# Funções para cores
def fontevermaelha(msg):
    print(f'\033[31m{msg}\033[m')


def fonteazul(msg):
    return f'\033[34m{msg}\033[m'


def fonteverde(msg):
    return f'\033[32m{msg}\033[m'


def fonteamarela(msg):
    return f'\033[33m{msg}\033[m'