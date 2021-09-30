# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome todo em letras maisculos
# o nome todo em minusculas
# quantas letras tem o nome ao todo
# e quantas letras tem o primeiro nome

       # maneira q fiz
nome = str(input('Escreva seu nome completo: '))
print(nome.upper()) #correto
print(nome.lower()) #correto
lista = nome.split()
n1 = len(lista[0])
n2 = len(lista[1])
n3 = len(lista[2])
tln = n1+n2+n3
print('O total de letras do seu nome é de {} letras'.format(tln))
print('A primeira letra do seu nome tem {}'.format(n1))

   # maneira correta

nome = str(input('Escreva seu nome completo: ')).strip()
print('O total de letras do seu nome é de {} letras'.format(len(nome)-nome.count(' ')))
print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))
print('seu primeiro nome {} tem {} letras'.format(lista[0], len(lista[0])))


