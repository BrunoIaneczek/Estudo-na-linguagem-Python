'''Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

turno = str(input("Diga o turno que você estuda: M-matutino, V-Vespertino, N- Noturno "))

if turno in "Nn":
    print('Boa noite!')
elif turno in "Mm":
    print('Boa dia!')
elif turno in "vV":
    print('Boa tarde!')
else:
    print('Resposta inválida')


