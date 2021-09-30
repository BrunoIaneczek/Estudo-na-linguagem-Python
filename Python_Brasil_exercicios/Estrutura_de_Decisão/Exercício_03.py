'''Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''

sexo = str(input('Digite seu sexo: ')).strip().lower()[0]
if sexo == 'f':
    print('Você e do sexo feminino.')
elif sexo == 'm':
    print('Você e do sexo masculino.')
else:
    print('Sexo inválido.')