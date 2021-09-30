'''Crie um programa que leia varios numeros inteiros
no final mostre a média entre eles e qual foi o maior e o menor, o programa deve perguntar
se o usuario quer ou nao continuar'''

um = 0
count = 0
soma = 0
opcao = ''
maior = 0
menor = 0
while opcao != 'n':
    num=int(input('digite um numero: '))
    opcao = str(input('Voce quer continuar [S/N]: ')).strip().lower()[0]
    if opcao not in 'ns':
       print('Opção inválida')
    count+=1
    soma += num
    if count == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('A média entre os numeros digitados é {:.2f}.'.format(soma/count))
print('E o maior numero é {} e o menor é {}.'.format(maior,menor))