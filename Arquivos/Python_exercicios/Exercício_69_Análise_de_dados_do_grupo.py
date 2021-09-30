'''Crie um programa que leia a idade e o sexo de várias
pessoas. A cada pessoa cadastrada, o programa deverá
perguntar se o usuaio quer continuar ou não e mostrar:
a) quantas pessoas tem mais de 18 anos
b)Quantos homens foram cadastrados.
c)quantas mulheres tem menos de 20 anos.'''
c1=c2=c3=0
while True:
    print(20*'-','\033[36mCadastro\033[m',20*'-')
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: ')).strip().lower()[0]
    if idade > 18:
        c1 += 1
    if sexo in 'm':
        c2 += 1
    if sexo in 'f' and idade < 20:
        c3 += 1
    while sexo not in 'fmFM':
        sexo = str(input('Digite o sexo: ')).strip().lower()[0]
    opcao = str(input('Quer continuar?[S/N] '))
    while opcao not in 'snSN':
        opcao = str(input('Quer continuar?[S/N] '))
    if opcao == 'n':
        break
print(20*'-','\033[31mFIM DO CADASTRO\033[m',20*'-')
print(f'Há {c1} pessoas com mais de 18 anos ')
print(f'Foram cadastrados {c2} homens.')
print(f'Há {c3} mulheres com menos de 20 anos.')


