'''TUPLAS'''
# TUPLAS SÃO IMUTÁVEIS

lanche = ('hambúrguer','suco','pizza','pudim')
print(lanche[0])
print(lanche[1])
print(lanche[2])
print(lanche[3])
print(lanche[1:3])
print(lanche[:2])
print(lanche[2:])
print(lanche[-4])
print(lanche[-3])
print(lanche[-2])
print(lanche[-1])
# METODO PARA ODENAR UMA TUPLA
print(sorted(lanche))

#for cont in range(0,len(lanche)):
 #   print(lanche[cont])
#for comida in lanche:
 #   print(f'Eu vou comer {comida}.')
'''A FUNÇÃO ENUMERATE()
Como percorremos os elementos de uma lista? Podemos utilizar a construção for in. Para cada elemento da lista, 
faça algo com tal elemento.

l = ['hello', 'world', 'hi', 'earth']
for word in l:
    print word
Outra forma de fazermos uma travessia em uma lista é através do acesso via índices.

l = ['hello', 'world', 'hi', 'earth']
for i in range(0, len(l)):
    print l[i]
O que é semelhante a:

l = ['hello', 'world', 'hi', 'earth']
i = 0
while i < len(l):
    print l[i]
    i = i + 1
Qual é a diferença básica entre os dois últimos códigos (que utilizam for i in range e while) 
para o primeiro trecho de código apresentado? É o acesso ao índice, à posição do elemento na lista. Utilizando 
a estrutura for el em in, não sabemos qual é a posição do item atual. Isso poderia ser necessário, por exemplo, 
se precisarmos escrever uma função que retorne uma lista contendo os índices das palavras que começam pelo caractere ‘a‘.

Para contornar esse problema, existe a função enumerate().
 Essa função pode receber como entrada uma lista e irá retornar um objeto do tipo enumerate, 
 que poderá ser percorrido pelo for. Vejamos um exemplo simples:

l = ['hello', 'world', 'hi', 'earth']
for i, word in enumerate(l):
    print i, word
Isso irá gerar a seguinte saída:

0 hello
1 world
2 hi
3 earth
E se quisermos escrever a função que retorna uma lista contendo as posições das palavras de uma lista
 que começam com a letra ‘a’?

def posicoesQueIniciamCom(lista, letra='a'):
    result = []
    for i, palavra in enumerate(lista):
        if palavra.startswith(letra):
            result.append(i)
    return result

nomes = ['abc', 'hua', 'aaa', 'asdfg', 'bnm']
print posicoesQueIniciamCom(nomes)
O resultado da execução do código acima será:

[0, 2, 3]
Assim, sempre que precisarmos dos índices dos elementos das listas (ou outros iteráveis) 
que estivermos percorrendo, podemos utilizar a função enumerate() para construir uma estrutura composta 
por pares índice-elemento'''

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na pos {pos}.')
print('Comi o que deu!')

# CONCATERNAR TUPLAS
a = (1,2,4,'fo',9)
b = (3,7,9,1,0)
c = a+b
d = b+a
print(c)
print(d)
print(d.count(9))
# PARA SE VERIFICAR POSIÇÃO DE UM ALIMENTO NA TUPLA

print(a.index('fo'))

# PARA VERIFICAR POSIÇÃO DE ELEMENTO REPETIDOS

print(d.index(9))
print(d.index(9,3)) # 3 e a proxima posição acima da primeira do elemento
# TUPLAS EM PYTHON ACEITAM DIVERSOS TIPOS PRMITIVOS
pessoa = ('bruno','26','91kg') # para deletar uma variavel utilize 'DEL'
print(pessoa)