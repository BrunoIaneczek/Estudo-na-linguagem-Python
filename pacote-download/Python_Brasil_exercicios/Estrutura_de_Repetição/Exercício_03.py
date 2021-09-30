'''Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';'''

while True:
    nome = str(input('Digite seu nome: ')).strip()
    while len(nome) > 3:
        nome = str(input('Nome inválido, digite novamente: ')).strip()
    idade = int(input('Digite sua idade: '))
    while idade <=0 or idade > 150:
        idade = int(input('Idade inválida, digite novamente: '))
    salario = float(input('Digite seu salário: '))
    while salario <= 0:
        salario = float(input('Salário inválido, digite novamente: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    while sexo not in 'MF':
        sexo = str(input('Sexo inválido, digite novamente[F/M]: ')).strip().upper()
    estadocivil = str(input('Digite seu estado civil [S,C,V,D]: ')).upper().strip()
    while estadocivil not in 'S,C,V,D':
        estadocivil = str(input('Estado civil não aceito, digite novamente[S,C,V,D]: ')).strip().upper()
    print('Individuo cadastrado com sucesso!')
    break

