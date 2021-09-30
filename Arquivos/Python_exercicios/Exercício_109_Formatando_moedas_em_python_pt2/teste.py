'''Modifique as funçoes criadas no ex107
para que elas aceitem um parâmetro adicional
informando se o valor informado por elas vai ser ou não formatado
como monetário'''

from ex109 import moeda

p = float(input('Digite um valor:R$'))
print(f'A metade de {moeda.conversor(p)} e {moeda.metade(p, True)}')
print(f'O dobro de {moeda.conversor(p)} é {moeda.dobro(p)}')
print(f'O valor aumentando 10% é {moeda.aumentar(p, 10, True)}')
print(f'O valor diminuindo 13% é {moeda.diminuir(p, 13, True)}')
