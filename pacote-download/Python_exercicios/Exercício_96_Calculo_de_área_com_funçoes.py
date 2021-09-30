'''Faça um programa que tenha uma função chamada área()
,que receba as dimensões de um terreno retangular e mostre
a área do terreno'''


def titulo(txt):
    print(20 * '-=-')
    print(f'{txt:^50}')
    print(20 * '-=-')
    print()


titulo('Controle de terrenos')
while True:
    larg = float(input('Digite a largura do terreno: '))
    comp = float(input('Digite o comprimento do terreno: '))


    def area(larg, comp):
        area = larg * comp
        print(f'O seu terreno de {larg:.2f}X{comp:.2f} tem a área de {area:.2f}m².')
        print()


    area(larg, comp)
    resp = str(input('Deseja verificar outro terreno? ')).upper()[0]
    while resp not in 'SsNn':
        resp = str(input('Por favor responda sim ou não: ')).upper()[0]
    if resp in 'Nn':
        break
