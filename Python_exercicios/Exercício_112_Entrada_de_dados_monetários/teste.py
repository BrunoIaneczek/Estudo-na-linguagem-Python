'''Dentro do pacote utilidadescev que criamos no dasafio 111, temos o modulo
chamado dado. crie uma função chmada leiadinhiero() que seja capaz de funcionar como a função input()
mas com uma validação de dados para aceitar apenas valores monetarios'''

from ex111.utilidadescev import moeda
from  ex111.utilidadescev import dado


p = dado.leiadinheiro("digite o preço: R$ ")
moeda.resumo(p,35,22)




