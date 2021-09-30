#Escreva um programa para aprovar o empréstimo bancário para compra de uma casa
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite seu salário: R$'))
anos = int(input('Digite em quantos anos você quer pagar o empréstimo '))
meses = anos*12
parcela = valor/meses
if parcela <= (salario*30)/100:
    print('O valor da sua parcela é R${:.2f} e seu empréstimo está aprovado.'.format(parcela))
else:
    print('O valor da sua parcela é R${:.2f} e infelizmente seu empréstimo  foi negado.'.format(parcela))