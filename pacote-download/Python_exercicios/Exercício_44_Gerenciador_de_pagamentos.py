# Elabore um programa que calcule o valor a ser pago
# por um produto, considerando o seu preço normal e condiçao de pagamento:
# á vista dinheiro/cheque: 10 %de desconto
# á vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

valor = float(input('Digite o valor a ser pago pelo produto R$'))
print('''Escolha uma das opções de pagamento abaixo:
[1] Dinheiro
[2] Á vista no cartão
[3] Em até 2x no cartão
[4] 3x ou mais no cartão
[5] cheque''')
avdc = valor-((valor*10)/100)
avc = valor-((valor*5)/100)
mpar = valor+((valor*20)/100)

fdp = int(input('Sua opção de pagamento: '))
if fdp == 1:
       print('A forma de pagamento escolhida foi em dinheiro, assim terá o desconto de 10% e o valor do produto ficará em \033[34mR${:.2f}\033[m.'.format(avdc))
elif fdp == 2:
       print('A forma de pagamento escolhida foi á vista no cartão, assim terá o desconto de 5% e o valor do produto ficará em \033[31mR${:.2f}\033[m.'.format(avc))
elif fdp == 3:
    p2= valor/2
    print('A forma de pagamento escolhida foi de 2x no cartão de R${:.2f}, sendo assim pagará o valor integral do produto que é de \033[32mR${:.2f}\033[m.'.format(p2,valor))
elif fdp == 4:
    p = int(input('Quantas parcelas? '))
    print('Você optou pelo pagamento em {:.0f}x de \033[33mR${:.2f}\033[m, sendo assim o valor total do produto sofrerá acréscimo de 20%, ficando no valor de \033[33mR${:.2f}\033[m.'.format(p,mpar/p,mpar))
elif fdp == 5:
    print('Você optou por pagar com cheque, assim terá o desconto de 10% e valor do produto será de \033[35mR${:.2f}\033[m.'.format(avdc))
else:
    print('Opção inválida de pagamento')