# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.No final mostre:
# A média da idade do grupo
# Qual o nome do homen mais velho
# Quantas mulheres tem menos de 20 anos
velho = 0
novo = 0
c = 0
si = 0
for x in range(1, 5):
    nome = str(input('Diga o nome da pessoa: ')).strip().lower()
    sexo = str(input('Diga o sexo da pessoa [M/F]: ')).strip().lower()
    idade = int(input('Diga a idade da pessoa: '))
    si += idade
    print(5*'---', x, 'pessoa', 5*'---')
    if sexo == 'f' and idade < 20:
        c += 1
    if sexo == 'm' and idade > velho:
        velho = idade
        b = nome

    m = si/4

print('A média de idade do grupo é de {} anos.'.format(m))
print('Entre as mulheres no grupo, {} tem menos de 20 anos.'.format(c))
print('O homen mais velho do grupo se chama {} e tem {} anos de idade.'.format(b, velho))


