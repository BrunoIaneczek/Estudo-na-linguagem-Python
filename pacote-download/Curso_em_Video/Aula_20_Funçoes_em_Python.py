'''Funçoes em Python, se utiliza do comando (def), segue os exemplos'''


# Funçao sem parametro:

def mostrarlinha():
    print(30 * '-=-')


mostrarlinha()
print('Olá mundo')
mostrarlinha()

# Função com parametro:

def titulo(txt):
    print(30*'-=-')
    print(txt)
    print(30*'-=-')


titulo('Ola alien bizarro')
titulo('Alien grotesco ')

def soma(num,num2,num3):
    s = num+num2+num3
    print(f'A = {num} B = {num2} e C = {num3}')
    print(f'A soma de A+B+C = {s}')


soma(4,3,3)

# Função com valores explicitados

soma(num=1,num2=2,num3=4) #deste modo defino qual valor para meu parametro

# Desempacotamento de funções(quando não se sabe a quantidade de parametros em uma função)


def contador(*num):
    tam = len(num)
    print(f'Os parametros são {num} e a quantidade é de {tam} ')


contador(9,0,8,2,3)

# Funcões co listas exemplo

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos +=1


valores = [3,4,5,6,7,8,2]
dobra(valores)
print(valores)
