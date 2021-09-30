'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''

opcao = ''
while opcao in 'Ss':
    letra = str(input('Digite uma letra: ')).strip().lower()
    if letra in 'aeiou':
        print('Esta letra e uma vogal!')
    elif letra in 'wertyipsdfghjklçzxvbnm':
        print('Esta letra e uma consoante!')
    else:
        print('Isto não uma letra palhaço.')
    opcao=str(input('Quer continuar [S/N] ')).strip().lower()[0]
print('Acabou')