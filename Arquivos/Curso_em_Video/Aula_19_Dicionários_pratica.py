pessoas = {'nome':'Bruno', 'sexo':'masculino', 'idade': 27}
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos') #para verificar os elementos utiliza-se aspas duplas
print()
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print()
for k in pessoas.keys():
    print(k)
print()
for k in pessoas.values():
    print(k)
print()
for k in pessoas.items():
    print(k)
print()
for k, v in pessoas.items(): # Substitui o enumerate nesta tecnologia
    print(f'{k} = {v}')
# Mudando valor da chave:
pessoas['nome'] = 'leandro'
# Adicionando elemento:
pessoas['peso'] = 89 # Substitui o apend

# Colocando dicionários dentro de listas:
Brasil = []
estado1 = {'UF': 'Rio Grande do Sul', 'Sigla': 'RS'}
estado2 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
Brasil.append(estado1)
Brasil.append(estado2)
print(Brasil)
print(Brasil[0])
print(Brasil[1])
print(Brasil[0]['UF'])

# Exemplo de estrutura
estado = dict()
brasil = []
for c in range(0,3):
    estado['uf'] = str(input('Digite um estado: '))
    estado['Sigla'] = str(input('Digite sua Sigla: '))
    brasil.append(estado.copy()) # O metodo copy copia o elemento
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()