# INTERACTIVE HELP
'''Utilizando este comando pode se conhecer o manual da função, pode ser diretamente no programa ou no python
 console(ao abrir o console se digita "help()" e logo depois a função, no programa pode se usar EX'''

help(print)
# ou(Ambas mostram a mesma documentação)
print(print.__doc__)
print()

# DOCSTRINGS
'''Esta nada mais é do a documentação do comando ou função, fornecida após o comando help
Mas nós podemos também definir uma docstring para uma função criada por nós,para se definir o docstring
 se abre 3 vezes aspas duplas, e então se escreve a documentação EX'''

def contador(i,f,p):
    """
    > Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo na contagem
    :return:
    """
    c = i
    while c < f:
        c+=p
        print(c,end=' ')

contador(0,14,2)
help(contador) #Tendo definido a docstring agora posso ter a mesma usando o comando help na função criada

# PARAMETROS OPCIONAIS
'''Através deste posso definir opções para parâmetros que estejam ausentes na função EX'''

def somar(a,b,c=0):
    s = a+b+c
    print(s)

somar(3,5,2) #todos os parametros na função
somar(3,2) #agora não e obtido o valor de C assim, pode se definir a opção na função a cima usando o parametro C=0
# posso definir para todos os parametros a opção EX (a=0,b=0,c=0)

# ESCOPO DE VARIAVEIS
'''O escopo define se uma variavel e local ou global dentro de um programa EX:'''

def teste():
    x = 8 # Escopo local, variavel so presente dentro da função
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

# programa principal
n = 2 # Escopo global, variável presente em todo o programa  dentro e fora da função
print(f'No programa principal, n vale {n}')
teste()

'''A como definir uma variavel local como global para isso se utiliza o comando (global) EX'''

def teste(b):
    global a # Neste momento a variavel passa a ter o valor definido dentro da função como global
    a = 8
    b+=4
    c = 2
    print(f'A dentro  vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

# Programa principal
a = 5 # Variavel global
teste(a)
print(f'A fora vale {a}')

# RETORNO DE VARIAVEIS
'''Com este comando consigo ter varias respostas de uma função dentro de um mesmo print EX'''

def soma (a=0, b=0, c=0):
    s = a+b+c
    # print(s) deste modo tenho apenas uma resposta de cada vez muito limitado
    return  s
s1 = soma(3,5)   #'''s1 s2 e s3 são as variaveis de resposta, estas que irão receber o que o s retornar'''
s2 = soma(3,5,1)
s3 = soma(10)
print(f'Os resultados das somas são {s1}, {s2} e {s3}.')

