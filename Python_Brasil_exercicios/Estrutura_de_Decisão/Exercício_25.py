'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".'''

while True:
    a = str(input('Você telefonou para a vitima?[S/N] ')).strip().lower()
    while a not in 'SsNn':
        a = str(input('Opção errada tente novamente ')).strip().lower()
    b = str(input('Você esteve n local do crime?[S/N] ')).strip().lower()
    while b not in 'SsNn':
        b = str(input('Opção errada tente novamente ')).strip().lower()
    c = str(input('Você mora perto da vítima?[S/N] ')).strip().lower()
    while c not in 'SsNn':
        c = str(input('Opção errada tente novamente ')).strip().lower()
    d = str(input('Você devia para a vítima?[S/N] ')).strip().lower()
    while d not in 'SsNn':
        d = str(input('Opção errada tente novamente ')).strip().lower()
    e = str(input('Já trabalhou com a vítima?[S/N] ')).strip().lower()
    while e not in 'SsNn':
        e = str(input('Opção errada tente novamente ')).strip().lower()

    if a == 's':
        a = 1
    else:
        a = 0
    if b == 's':
        b = 1
    else:
        b = 0
    if c == 's':
        c = 1
    else:
        c = 0
    if d == 's':
        d = 1
    else:
        d = 0
    if e == 's':
        e = 1
    else:
        e = 0
    resultado = a+b+c+d+e
    if resultado == 2:
        print('Você é suspeita!')
    if resultado == 3 or resultado == 4:
        print('Você é cumplice!')
    if resultado == 5:
        print('Você é o assassino!')
    if resultado == 1:
        print('Você é o inocente!')
    resp = str(input('Deseja investigar mais algum suspeito?[S/N] ')).strip().lower()
    while resp not in 'SsNn':
        resp = str(input('Opção inválida, digite novamente ')).strip().lower()
    if resp != 's':
        break


