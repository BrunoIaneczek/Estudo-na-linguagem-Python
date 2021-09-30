
'''Reescreva a função leiaint() do desafio 104  incluindo agora a possiblilidade
de digitar um numero inválido aproveite e crie tambem a função leiafloat()'''


def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError,TypeError):
            print('\033[31mERRO: Por favor digite um numero inteiro válido!\033[m')
        except (KeyboardInterrupt):
            print('\033[31mERRO: usuário não informou nada\033[m')
        else:
            return valor


def leiafloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except:
            print('\033[31mERRO: Por favor digite um numero real válido!\033[m')
        else:
            return valor


n = leiaint('digite um numero inteiro ')
f = leiafloat('Digite um numero real ')
print(f'O valor inteiro é {n} e o real é {f}.')
