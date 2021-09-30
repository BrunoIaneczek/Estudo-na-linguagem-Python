'''Escreva um programa para aprovar o empréstimo bancário para a compra
de uma casa .Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal.Não pode exceder 30% do salário ou então o empréstimo será negado'''

ValordaCasa = float(input('Digite o valor da casa: R$'))
Salário = float(input("Digite o valor de seu salário: R$"))
QuantosAnosparaPagamento = int(input('Digite em quantos anos pretende pagar: '))

meses = QuantosAnosparaPagamento*12

ValorParcela = ValordaCasa/meses

ValortaxasobreSalário = (Salário*30)/100

print(f'O valor de sua parcela será de R${ValorParcela:.2f}')
print(f'Sua taxa foi de R${ValortaxasobreSalário:.2f}')

if ValorParcela>ValortaxasobreSalário:
    print('Seu empréstimo foi negado!')
else:
    print('Seu empréstimo foi aprovado!')

