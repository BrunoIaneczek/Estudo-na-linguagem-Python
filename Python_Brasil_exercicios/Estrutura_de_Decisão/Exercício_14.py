'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E'''

resp = ''
while True:
    n1 = float(input('Digite a primeira nota do aluno: '))
    n2 = float(input('Digite a segunda nota do aluno: '))
    media = (n1+n2)/2
    if media >= 9 and media <=10:
        print('O aluno recebe o conceito A, aprovado')
    elif media >= 7.5 and media < 9:
        print('O aluno recebe o conceito B,aprovado')
    elif media >=6 and media < 7.5:
        print('O aluno recebe o conceito C,aprovado')
    elif media >= 4 and media < 6:
        print('O aluno recebe o conceito D, reprovado')
    elif media >=0 and media < 4:
        print('O aluno recebe o conceito E reprovado')
    resp = str(input('Deseja continuar com outra notas? [S/N] ')).strip().lower()[0]
    if resp == 'n':
        break
    while resp not in  'sn':
        resp = str(input('Deseja continuar com outra notas? [S/N] ')).strip().lower()[0]
print('Programa encerrado')

