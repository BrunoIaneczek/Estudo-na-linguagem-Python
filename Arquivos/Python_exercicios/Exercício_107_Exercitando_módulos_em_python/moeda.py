def aumentar(valor,porcentagem=0):
    valorporcentagem = (valor * porcentagem) / 100
    valorfinal = valor + valorporcentagem
    return valorfinal


def diminuir(valor,porcentagem=0):
    valorporcentagem = (valor * porcentagem) / 100
    valorfinal = valor - valorporcentagem
    return valorfinal


def dobro(valor):
    dobro = valor * 2
    return dobro


def metade(valor):
    metade = valor/2
    return  metade
