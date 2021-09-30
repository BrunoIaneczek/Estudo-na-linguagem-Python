'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
 O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% '''
'''Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00'''

ir = 5
inss = 10
fgts = 11
sindicato = 3
resp = ''
while True:
    valorhora = float(input('Por favor digite o valor da sua hora trabalhada: '))
    horastrabalhadas = int(input('Digite o numero de horas trabalhadas: '))
    salariobruto = valorhora*horastrabalhadas
    if salariobruto <= 900:
        ir = 0
    elif salariobruto <=1500:
        ir = 5
    elif salariobruto <=2500:
        ir = 10
    else:
        ir = 20
    print(' ')
    print(f'Salário Bruto: ({valorhora:.2f} X {horastrabalhadas})     :R${(valorhora*horastrabalhadas):.2f}')
    print(f'(-)IR ({ir})                       :R${((salariobruto*ir)/100):.2f}')
    dir = (salariobruto*ir)/100
    print(f'(-) INSS (10%)                  :R${((salariobruto*10)/100):.2f}')
    dinss = (salariobruto*10)/100
    print(f'FGTS (11%)                      :R${((salariobruto*11)/100):.2f}')
    dfgts = (salariobruto*11)/100
    print(f'Sidicato                        :R${((salariobruto*3)/100):.2f}')
    dsind = (salariobruto*3)/100
    print(f'Total dos descontos             :R${(dir+dinss+dsind):.2f}')
    desct = dir+dinss+dsind
    print(f'salário liquido                 :R${(salariobruto-desct):.2f}')
    print(' ')
    resp = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    while resp not in 'sn':
        resp = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if resp == 'n':
        break
print('\033[31mPrograma encerrado!\033[m')


