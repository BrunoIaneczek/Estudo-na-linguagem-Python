# Faça um Programa que mostre a mensagem "Alo mundo" na tela.

print('\033[31m ola mundo\033[m')
print('\033[32m olá planeta \033[m')
print('\033[35;8;33m olá terra \033[m')

nome = str(input('Digite seu nome: ').strip().lower())
tlnome = len(nome)
nomelista = list(nome)
if nome == 'bruno':
    print('nome bonito')
    if nome[tlnome - 1] == 'o':
        print('Seu nome termina em \033[33m o. \033[m')
else:
    print('Outro nome.')
    if tlnome > 5:
        print('Seu nome tem mais de \033[32m5 letras.\033[m')
        print('Seu nome termina em', nome[tlnome - 1], '.')
        if tlnome > 10:
            print('Nome tem mais de 10 letras')
