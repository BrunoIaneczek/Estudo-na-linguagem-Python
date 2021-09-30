#Nomenclatura

#dados = dict()
'ou'
dados = {'nome':'pedro', 'idade':'25'}
print(dados['nome'])
print(dados['idade'])
print()
# Adicionar elementos
dados['sexo']='m'
# Para remover
del dados['idade'] #entre aspas o elemento a ser removido

#Estruturas

filme = {'titulo':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'}
filme2 = {'titulo':'Avengers',
          'ano':2012,
          'diretor':'Joss whedon'}
print(filme.values()) # Retorna todos os valores do dicionario
print(filme.keys()) # Retorna as chaves(titulo, ano, diretor.etc)
print(filme.items()) #Retorna todos valores keys e values
print()
#Exemplo com For

for k,v in filme.items():
    print(f'O {k} é {v}')
print()

#Juntando listas, tuplas e dicionários

locadora = [filme, filme2]
print(locadora[0]['ano']) #retorna valor na chave solicitada
print(locadora[1]['titulo'])