'''Crie um pacote chamado utilidadescev que tenha dois módulos internos
chamados moeda e dado, transfira todos as funçoes utilizadas nos desafios 107,108,109
para o primeiro pacote'''

from ex111.utilidadescev import moeda
#from ex111.utilidadescev import dado

p = float(input('Digite um valor:R$'))
moeda.resumo(p,35,22)
