'''Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg)
de maças adquiridas e escreva o valor a ser pago pelo cliente.'''
MorangoAte5Kg = 2.50
MorangoAcimaDe5KG = 2.20
MacaAte5Kg = 1.80
MacaAcimaDe5Kg = 1.50
morangokg = 0
macakg = 0
macavalor = 0
morangovalor = 0
valortotal = 0
desconto = 0
print('BEM VINDO')
while True:
    resp = str(input('Deseja comprar alguma fruta? ')).strip().upper()
    if resp in 'nN':
        break
    maca = str(input('Deseja comprar maça? [S/N] ')).strip().upper()
    if maca in 'Ss':
        macakg = float(input('Ótimo quantos Kg? '))
        if macakg > 5:
            macavalor = macakg * MacaAcimaDe5Kg
        else:
            macavalor = macakg * MacaAte5Kg
    else:
        print('Tudo bem!')
    morango = str(input('Deseja comprar morangos? [S/N] ')).strip().upper()
    if morango in 'Ss':
        morangokg = float(input('Muito bem, quantos Kg? '))
        if morangokg > 5:
            morangovalor = morangokg * MorangoAcimaDe5KG
        else:
            morangovalor = morangokg * MorangoAte5Kg
    else:
        print('Certo')
    break
valortotal = morangovalor + macavalor
if (morangokg + macakg) > 8 or valortotal >= 25:
    desconto = (valortotal * 25) / 100
    valortotal = valortotal - desconto
print(f'Vai sair o total de R${valortotal:.2f}, pelos {macakg:.2f}Kg de maça e os {morangokg:.2f}Kg de morango,\n'
      f'sendo que a maça ficou em R${macavalor:.2f} o morango R${morangovalor:.2f}.')

