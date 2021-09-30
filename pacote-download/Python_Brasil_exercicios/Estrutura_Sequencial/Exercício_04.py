# Faça um programa que mostre 4 notas de um aluno e mostre a média

print(10*'=='), print('\033[32mCalculador de média\033[m'), print(10*'==')
snotas = 0
for n in range(1,5):
    nota = float(input('Digite a {}º nota do aluno: '.format(n)))
    snotas += nota
media = snotas/n
print('A média do aluno foi de \033[32m{}\033[m.'.format(media))