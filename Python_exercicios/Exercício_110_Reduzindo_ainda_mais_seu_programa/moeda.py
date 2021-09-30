
def aumentar(valor, porcentagem=0, moeda=False):
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

def resumo(p,percentualParaMais, percentualParaMenos):
    print(30*'-')
    print('RESUMO DO VALOR'.center(30))
    print(30 * '-')
    print(f"""
    Preço analisado: \t{conversor(p)}
    Metade do preço: \t{metade(p, True)}
    Dobro do preço:  \t{dobro(p,True)}
    {percentualParaMais} de aumento:   \t{aumentar(p, percentualParaMais, True)}
    {percentualParaMenos} de redução:   \t  {diminuir(p, percentualParaMenos, True)}""")
    print(30 * '-')