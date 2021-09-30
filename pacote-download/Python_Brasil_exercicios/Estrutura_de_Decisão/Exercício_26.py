"""Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que,
 o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90."""
descontogasolinaacimade20l = 6
descontogasolinaabaixode20l = 4
descontoalcoolabaixode20l = 3
descontoalcoolacimade20l = 5
precoalcool = float(1.90)
precogasolina = float(2.50)

while True:
    combustivel = str(input('Escolha o tipo de combustivel: [A/G] ')).strip()
    while combustivel not in 'aAgG':
        combustivel = str(input('Combustivel errado, escolha novamente '))
    if combustivel in 'Aa':
        litrosa = int(input('Quantos litros de alcool quer abastecer? '))
        if litrosa <= 20:
            novovaloralcoolab20 = precoalcool - ((precoalcool * descontoalcoolabaixode20l) / 100)
            print(
                f'Você terá desconto de {descontoalcoolabaixode20l}% o preço por litro ficará em R${novovaloralcoolab20:.2f} '
                f' assim irá pagar o valor de R${novovaloralcoolab20 * litrosa:.2f}')
        else:
            novovaloralcoolac20 = precoalcool - ((precoalcool * descontoalcoolacimade20l) / 100)
            print(
                f'Você terá o desconto de {descontoalcoolacimade20l}% o preço por litro ficará R${novovaloralcoolac20:.2f} assim '
                f'irá pagar o valor de R${novovaloralcoolac20 * litrosa:.2f}')
    else:
        litrosg = int(input('Quantos litros de gasolina quer abastecer? '))
        if litrosg <= 20:
            novovalorgasolinaab20 = precogasolina - ((precogasolina * descontogasolinaabaixode20l) / 100)
            print(
                f'Você terá o desconto de {descontogasolinaabaixode20l}%, o preço por litro ficará R${novovalorgasolinaab20:.2f}'
                f' assim o valor a ser pago será de R${novovalorgasolinaab20 * litrosg:.2f}')
        else:
            novovalorgasolinaac20 = precogasolina - ((precogasolina * descontogasolinaacimade20l) / 100)
            print(f'Você terá o desconto de {descontogasolinaacimade20l}%, o preço ficará R${novovalorgasolinaac20:.2f}'
                  f' assim o valor a ser pago será de R${novovalorgasolinaac20 * litrosg:.2f}')
    reset = str(input('Deseja realizar outro abastecimento? [S/N]? ')).strip().upper()
    while reset not in 'SsNn':
        reset = str(input('Por favor responda sim ou não[S/N] ')).upper()
    if reset in 'N':
        print(50*'-=-')
        print('Obrigado por utilizar nossos serviços!')
        break
