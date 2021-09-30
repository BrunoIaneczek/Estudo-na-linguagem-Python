######### LISTAS ########

# Exemplo de lista:
    # Em listas utilizamos dos [], para atribuir valores.

lanche = ['xis','cachorro quente','batata frita']

# Comandos em listas:
lanche.append('pastel') # Este comando adiciona um item ao final da lista
#print(lanche)

lanche.insert(0,'miojo') # Este comando inseri um item em qualquer posição na lista, colocando a posiçao desejada no inicio
#print(lanche)

# Apagando elementos da lista
    # comandos
del lanche[1]
lanche.pop() # Este elimina o ultimo elemento da lista, nas pode se determinar um parametro no parenteses
lanche.remove('batata frita') # Este elemina um item se utilizando do valor e nao do indice, como no exemplo

# Criando listas com range:
#exemplo
numeros=list(range(0,10))
print(numeros)

# Se os valores estiverem fora de ordem pode se usar o seguinte comando, para ordena-los
numeros.sort()
# Caso se queira ordena-los na ordem inversa se utiliza o comando:
numeros.sort(reverse=True)

# Para se saber o tamanho da lista e so utlizar o comando len
len(numeros)

# ESTRUTURAS EXEMPLOS
    # Decisão
if 'xis' in lanche:
    lanche.remove('xis')
print(lanche)
