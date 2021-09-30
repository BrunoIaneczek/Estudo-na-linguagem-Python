def aumentar(valor,porcentagem=0):
    valorporcentagem = (valor * porcentagem) / 100
    return valor + valorporcentagem



def diminuir(valor,porcentagem=0):
    valorporcentagem = (valor * porcentagem) / 100
    return valor - valorporcentagem



def dobro(valor):
     return valor * 2


def metade(valor):
     return  valor/2


def conversor(valor,moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')





