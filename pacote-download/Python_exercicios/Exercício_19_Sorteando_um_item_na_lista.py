# faça um programa que sortei entre quatro alunos e mostre o escolhido

import random
a1 = input('primeiro aluno: '
a2 = input('segundo aluno: ')
a3 = input('terceiro aluno: ')
a4 = input('quarto aluno: ')
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno que vai limpar o quadro é',escolhido)
