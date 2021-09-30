'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
e lhe contraram para desenvolver o programa que calculará os reajustes.'''
'''Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

resp = ''
while resp in 's':
    salario = float(input('Qual o valor do se salario? R$'))
    if salario < 280:
        porcentual = 20
        aumento=(salario*porcentual)/100
        ns = salario+aumento
        print(f'Seu salário era de {salario:.2f}, o percentual aplicado foi de {porcentual}% e seu aumento foi de {aumento:.2f},'
              f'e seu novo salário é R${ns:.2f}')
    if  salario >= 280 and salario <= 700:
        porcentual = 15
        aumento = (salario*15)/100
        ns = salario+aumento
        print(f'Seu salário era de {salario:.2f}, o percentual aplicado foi de {porcentual}% e seu aumento foi de {aumento:.2f},'
              f'e seu novo salário é R${ns:.2f}')
    if salario >= 1500:
        porcentual = 5
        aumento =(salario*5)/100
        ns = salario+aumento
        print(f'Seu salário era de {salario:.2f}, o percentual aplicado foi de {porcentual}% e seu aumento foi de {aumento:.2f},'
              f'e seu novo salário é R${ns:.2f}')
    if salario >700 and salario <1500:
        porcentual = 10
        aumento = (salario*10)/100
        ns = salario+aumento
        print(f'Seu salário era de {salario:.2f}, o percentual aplicado foi de {porcentual}% e seu aumento foi de {aumento:.2f},'
              f'e seu novo salário é R${ns:.2f}')
    resp = str(input('Você quer continuar [S/N]? ')).strip().lower()[0]
    while resp not in 'sn':
        resp = str(input('Você quer continuar [S/N]? ')).strip().lower()[0]
print('Programa encerrado.')



