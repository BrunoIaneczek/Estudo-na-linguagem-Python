'''O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                    acima de 5 Kg           ate de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
 porém não há limites para a quantidade de carne por cliente.
 Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
 Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
contendo as informações da compra:
tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.'''
carnes = ['file duplo: {:>27}'.format('R$4,90    R$5,80'),  'alcatra: {:>30}'.format('R$5,90    R$6,80'),
          'picanha: {:>30}'.format('R$6,90    R$7,80')]
cortes = ['File Duplo', 'Alcatra', 'Picanha']
PrecosFileDuplo = [4.90, 5.80]
PrecosAlcatra = [5.90, 6.80]
PrecosPicanha = [6.90, 7.80]
qtd = 0
valortotal = 0
while True:
    print('\033[34m{:^30}\033[m'.format('Bom dia'))
    print('{:^30}'.format('Menu'))
    print('{}{:^40}{:>5}'.format('indice','Acima de 5Kg','Até 5Kg'))
    for i,c in enumerate(carnes):
            print('{} {:<20}'.format(i,c))

    pagamento = str(input('Vai realizar o pagamento no cartão? ')).lower()
    while pagamento not in 'ns':
        pagamento = str(input('Por favor responda [S/N] ')).lower()
    if pagamento in 'Ss':
        pagamento = 'Cartão'
        carne = int(input('Qual carne deseja comprar, conforme o numero menu? '))
        if carne == 0:
            qtd = float(input('Quantos Kgs de filé duplo deseja comprar? '))
            if qtd > 5:
                valortotal = qtd*PrecosFileDuplo[0]
            else:
                valortotal = qtd*PrecosFileDuplo[1]
        elif carne == 1:
            qtd = float(input('Quantos Kgs de alcatra deseja comprar? '))
            if qtd > 5:
                valortotal = qtd*PrecosAlcatra[0]
            else:
                valortotal = qtd*PrecosAlcatra[1]
        elif carne == 2:
            qtd = float(input('Quantos Kgs de picanha deseja comprar' ))
            if qtd > 5:
                valortotal = qtd*PrecosPicanha[0]
            else:
                valortotal = qtd*PrecosPicanha[1]
        desconto = (valortotal * 5) / 100
        valortotalcomdesconto = valortotal - desconto
        print(30*'-=-')
        print(f'Carne: {cortes[carne]}\nPeso: {qtd:.2f}Kg\nValor Total: R${valortotal:.2f}'
              f'\nValor total com Desconto: R${valortotalcomdesconto:.2f}\nTipo de pagamento: {pagamento}\n'
              f'Desconto: R${desconto:.2f}')
        print(30*'-=-')
    else:
        print('Ok, mas não terá desconto')
        pagamento = 'Outra forma de pagamento'
        carne = int(input('Qual carne deseja comprar, conforme o numero menu? '))
        if carne == 0:
            qtd = float(input('Quantos Kgs de filé duplo deseja comprar? '))
            if qtd > 5:
                valortotal = qtd * PrecosFileDuplo[0]
            else:
                valortotal = qtd * PrecosFileDuplo[1]
        elif carne == 1:
            qtd = float(input('Quantos Kgs de alcatra deseja comprar? '))
            if qtd > 5:
                valortotal = qtd * PrecosAlcatra[0]
            else:
                valortotal = qtd * PrecosAlcatra[1]
        elif carne == 2:
            qtd = float(input('Quantos Kgs de picanha deseja comprar'))
            if qtd > 5:
                valortotal = qtd * PrecosPicanha[0]
            else:
                valortotal = qtd * PrecosPicanha[1]
        print(30*'_=_')
        print(f'Carne: {cortes[carne]}\nPeso: {qtd:.2f}Kg\nValor Total: R${valortotal:.2f}'
              f'\nTipo de pagamento: {pagamento}\n')
        print(30*'-=-')
    resp = str(input('Deseja mais alguma coisa? ')).upper()
    while resp not in 'SN':
        resp = str(input('Por favor responda [S/N] ')).upper()
    if resp in 'N':
        print('Obrigado pela preferência!')
        break


