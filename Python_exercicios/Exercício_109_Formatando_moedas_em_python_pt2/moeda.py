def aumentar(valor, porcentagem=0, moeda=False):
    """
    Função que permite aumentar o valor em determinada
    porcentagem

    :param valor: valor que se quer aumentar
    :param porcentagem: porcentagem que se quer aumentar
    :param moeda: se quiser o valor formatado, so incluir True
    :return: valor acrescido da porcentagem
    """
    valorporcentagem = (valor * porcentagem) / 100
    res = valor + valorporcentagem
    return res if moeda is False else conversor(res)


def diminuir(valor, porcentagem=0, moeda=False):
    valorporcentagem = (valor * porcentagem) / 100
    res = valor - valorporcentagem
    return res if moeda is False else conversor(res)


def dobro(valor, moeda=False):
    res = valor * 2
    return res if moeda is False else conversor(res)


def metade(valor, moeda=False):
    res = valor / 2
    return res if moeda is False else conversor(res)


def conversor(valor, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
