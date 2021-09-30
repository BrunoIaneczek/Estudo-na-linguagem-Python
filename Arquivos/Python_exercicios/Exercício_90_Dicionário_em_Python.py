'''Faça um programa que leia nome e média de um aluno,
guardando também a situação e um dicionário. No final,
mostre o conteúdo da  estrutura na tela'''

aluno = dict()
aluno['aluno'] = str(input('nome: '))
aluno['media'] = float(input(f'Média de {aluno["aluno"]}: '))
if aluno['media'] >= 7:
   aluno['situação'] = 'Aprovado'
elif aluno['media'] >=5     < 7:
    aluno['situação'] = 'Recuperção'
else:
    aluno['situação'] = 'Reprovado'
for k , v in aluno.items():
    print(f'{k} é igual {v}.')
'''print(f'Nome é igual {aluno["aluno"]}.')
print(f'Média é igual {aluno["media"]}.')
print(f'A situação é {aluno["situação"]}.')'''

