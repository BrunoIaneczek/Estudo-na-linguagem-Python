'''Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.'''

from datetime import  date
data_atual = date.today()
print(data_atual)
data_atual_texto = f'{data_atual.day}/{data_atual.month}/{data_atual.year}'
print(data_atual_texto)
data_texto_fim = data_atual.strftime(data_atual.day)
print(data_texto_fim)

