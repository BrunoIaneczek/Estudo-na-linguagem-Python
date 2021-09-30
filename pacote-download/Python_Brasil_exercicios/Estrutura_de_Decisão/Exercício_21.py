'''Faça um Programa para um caixa eletrônico.
O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
 As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
 O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5
e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.'''

print(20*'-','CAIXA ELETRÔNICO',20*'-')

valor = int(input('Digite o valor do saque: '))
total = valor
if total >=0 and total<= 1000000:
    céd = 100
    totcéd = 0
    while True:
        if total >= céd:
            total -= céd
            totcéd += 1
        else:
            if totcéd > 0:
                print(f'Tota de {totcéd} de {céd}. ')
            if céd == 100:
                céd = 50
            elif céd == 50:
                céd = 20
            elif céd == 20:
                céd = 10
            elif céd == 10:
                céd = 5
            elif céd == 5:
                céd = 1
            totcéd = 0
            if total == 0:
                break




