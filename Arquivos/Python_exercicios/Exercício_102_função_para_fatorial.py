def fatorial(n,show=0):
    """
    Calcula um fatorial de um numero
    :param n: O numero a ser calculado
    :param show: Mostra ou não a conta
    :return: o valor fatorial de n
    """
    c = n
    f = 1
    while c > 0:
        if show:
            print(f'{c}',end=' ')
            print(' x ' if c > 1 else ' = ',end='')
        f *= c
        c -= 1
    return f'{f}'
''
print(fatorial(5))
print(fatorial(5,True))
help(fatorial)