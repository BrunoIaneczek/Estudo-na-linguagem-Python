'''Adapte o código do exercicío 107
vcrinado uma função adicional que consiga mostrar valores
em formato monetário'''

from ex108 import moeda

p = float(input('Digite um valor:R$'))
print(f'A metade de {moeda.conversor(p)} e {moeda.conversor(moeda.metade(p))}' )
print(f'O dobro de {moeda.conversor(p)} é {moeda.conversor(moeda.dobro(p))}')
print(f'O valor aumentando 10% é {moeda.conversor(moeda.aumentar(p,10))}')
print(f'O valor diminuindo 13% é {moeda.conversor(moeda.diminuir(p,13))}')
