"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre
o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
5% para o sindicato , faça um programa que nos dê: salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato. o
salário líquido. calcule os descontos e o salário líquido, conforme a tabela abaixo: + Salário Bruto : R$ - IR (11%)
: R$ - INSS (8%) : R$ - Sindicato ( 5%) : R$ = Salário Liquido : R$ """
from time import sleep
print(30 * '\033[32m=\033[m', '\033[32mDADOS FOLHAS DE PAGAMENTO\033[m', 30 * '\033[32m=\033[m')
print(20 * '    ')
salariobase = float(input('Digite o valor do seu salário base: '))
salariohora = salariobase/220
totalhoras = float(input('Digite quantas horas foram trabalhadas neste mês: '))
salariobruto = salariohora * totalhoras
print(30 * '   ')
menu = '''[1] Salário Bruto 
[2] Valor IR (11%) 
[3] Valor INSS (8%) 
[4] Valor Sindicato ( 5%) 
[5] Valor Salário Liquido
[6] Reesibir menu
[7] Encerrar programa'''
opção = 0
print(15 * '==', 'Menu', 15 * '==')
print(menu)
valorinss = salariobruto * 8 / 100
salariobrutomenosinss = salariobruto - valorinss
valorIR = salariobrutomenosinss * 11/100
valorsindicato = salariobruto * 5 / 100
salarioliquido = salariobruto - (valorinss + valorIR + valorsindicato)
while opção != 7:
    print(30 * '==')
    opção = int(input('Digite a opção desejada: '))
    if opção == 2:
        print('O valor do IR a ser descontado será de \033[34mR${:.2f}.\033[m'.format(valorIR))
    elif opção == 1:
        print('Seu salário bruto é de \033[36mR${:.2f}.\033[m'.format(salariobruto))
    elif opção == 3:
        print('O valor do INSS a ser descontado é de \033[31mR${:.2f}.\033[m'.format(valorinss))
    elif opção == 4:
        print('O valor do desconto sindical a ser cobrado é de \033[31mR${:.2f}.\033[m'.format(valorsindicato))
    elif opção == 5:
        print('Seu salário liquido neste mês é de \033[36mR${:.2f}\033[m.'.format(salarioliquido))
    elif opção == 6:
        print(menu)
    else:
        sleep(1,5)
        print('Programa encerrado')
print('ate logo!')


