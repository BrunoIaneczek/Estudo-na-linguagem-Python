# Adicionando listas dentro de listas
dados = []
dados.append('pedro')
dados.append('35')
pessoas = []
pessoas.append(dados[:]) #Observe a estrutura "[:]" , está gera uma cópia exata da lista, a ser adicionada.

#Exemplo de lista dentro de lista
pessoas = [['pedro',25],['maria',19],['joao',32]]

# Selecioando item dentro de uma lista dentro de otra lista:
''' print(pessoas[0][0]) => pedro
    print(pessoas[1][1]) => 19
    print(pessoas[2][0]) => joao
    print(pessoas[1]) => ['maria',19] '''
#Deste modo o primeiro colchetes selecionará o item na lista principal, e o segundo selecionara
# o da lista secundária, caso nao haja o segundo , ira trazer o conteudo total da sublista.