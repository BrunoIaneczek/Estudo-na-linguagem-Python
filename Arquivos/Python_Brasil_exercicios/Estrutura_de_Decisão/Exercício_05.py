'''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.'''
c = ''
while c in 'Ss':
    nota1 = float(input('Digite o valor da primeira nota: '))
    nota2 = float(input('Digite o valor da segunda nota: '))
    média = (nota1+nota2)/2
    if média >= 7 and  média < 10:
        print('Aprovado')
    elif média < 7:
        print('Reprovado')
    elif média == 10:
        print('Aprovado com excelência')
    c = str(input('Deseja continuar [S/N] ? ')).lower().strip()[0]
    if c not in 'ns':
        print('valor inválido')
print('encerrado')