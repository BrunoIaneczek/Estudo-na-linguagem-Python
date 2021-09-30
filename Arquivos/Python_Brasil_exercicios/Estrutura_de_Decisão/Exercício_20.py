'''Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada
por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''

while True:
    resp = ''
    n1 = float(input('Digite a primeira nota do aluno: '))
    n2 = float(input('Digite a segunda nota do aluno: '))
    n3 = float(input('Digite a terceira nota do aluno: '))
    print('')
    media = (n1+n2+n3)/3
    if media >= 7 and media != 10:
        print(f'O aluno está aprovado, com a média de {media:.2f}.')
    elif media < 7:
        print(f'O aluno está reprovado, com a média de {media:.2f}.')
    elif media == 10:
        print(f'O aluno foi aprovado com distinção, com a incrivel média  {media:.2f}.')
    print('')
    resp = str(input('Deseja verificar a media de algum outro aluno [S/N]? ')).strip().lower()[0]
    print('')
    while resp not in 'sn':
        resp = str(input('Deseja verificar a media de algum outro aluno [S/N]? ')).strip().lower()[0]
    if resp == 'n':
        break
print('Fim da avaliação!')

