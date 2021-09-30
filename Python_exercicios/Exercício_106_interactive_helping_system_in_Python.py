'''Faça um mini-sistema que utiliza o interactive help
O usuário irá digitar um comando e seu manual irá aparecer
ao digitar 'FIM'  o programa se encerrará'''
def manual(com):
    print('\033[0;30;44m')
    help(com)
    print('\033[0;30;44m')
def titulo(txt):
    tamanhodotexto = len(txt)
    print(tamanhodotexto*'\033[1;42m=\033[m')
    print(f'\033[1;42m{txt}\033[m')
    print(tamanhodotexto*'\033[1;42m=\033[m')

def titulo2(txt):
    tamanhodotexto = len(txt)
    print(tamanhodotexto * '\033[1;104m=\033[m')
    print(f'\033[1;104m{txt}\033[m')
    print(tamanhodotexto * '\033[1;104m=\033[m')


def titulo3(txt):
    tamanhodotexto = len(txt)
    print(tamanhodotexto * '\033[1;101m=\033[m')
    print(f'\033[1;101m{txt}\033[m')
    print(tamanhodotexto * '\033[1;101m=\033[m')


from time import sleep
titulo2('SISTEMA DE AJUDA pyHELP')
parametro = str(input('Digite uma função ou biblioteca: ')).strip()
while True:
    if parametro not in 'fim':
        titulo(f'Acessando o manual do "{parametro}".')
        sleep(1)
        manual(parametro)
        titulo2('SISTEMA DE AJUDA pyHELP')
        parametro = str(input('Digite outra função: ')).strip()
    else:
        titulo3('Até logo!')
        break


