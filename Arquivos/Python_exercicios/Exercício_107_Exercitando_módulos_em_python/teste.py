'''Crie um modulo chamado moeda.py que tenha as funçoes incorporadas
aumentar(),diminuir(),dobro e metade()
Faça tambem um programa que importe e use as funçoes do mesmo'''

from ex107 import moeda

p = float(input("Digite o preço: R$"))
print(f'O dobro de R${p} é R${moeda.dobro(p)}.')
print(f'A metade de R${p} é R${moeda.metade(p)}.')
print(f'Aumentado em 10%, temos R${moeda.aumentar(p,10)}')
print(f'Diminuindo em 13%, temos R${moeda.diminuir(p,13)}')
