# faça um programa semelhante ao desafio anterior mas que ao invés de sortear um aluno, agora sorteia a ordem de apresentação entre 4 alunos.

from random import shuffle
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de execução do trabalho será {}'.format(lista))