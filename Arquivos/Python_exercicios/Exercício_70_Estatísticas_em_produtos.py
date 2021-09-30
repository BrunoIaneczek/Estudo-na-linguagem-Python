"""Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar no final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato."""

print(20 * '-', '\033[36mSuper mercadão\033[m', 20 * '-')
totalgasto = menor = produtos = produtosacimade1000 = 0
continuar = barato = ''
while True:
    produto = str(input('Qual o produto adquirido? ')).strip()
    produtos += 1
    preço = float(input('Qual o valor do produto? '))
    if produtos == 1 or preço < menor:
        menor = preço
        barato = produto
    if preço > 1000:
        produtosacimade1000 += 1
    totalgasto += preço
    continuar = str(input('Deseja continuar?[S/N] ')).strip().lower()[0]
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar?[S/N] ')).strip().lower()[0]
    if continuar == 'n':
        break
print(20 * '-', 'FIM DAS COMPRAS!', 20 * '-')
print(f'Você gastou \033[36mR${totalgasto:.2f}\033[m nas suas compras.')
print(f'Dentre os produtos, {produtosacimade1000} são custam mais de mil reais.')
print(f'O produto mais barato foi o/a {barato} e custa \033[34mR${menor:.2f}\033[m.')
