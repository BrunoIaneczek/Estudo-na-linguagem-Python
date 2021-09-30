# Faça um programa que pergunte quanto você ganha por hora e o numero de horas trabalhadas no mês.
# Calcule e mostre seu salário no mês.
print(60*'\033[36m==\033[m'), print('\033[34mPrograma calcula seu salário conforme suas horas trabalhadas.\033[m'), print(60*'\033[36m==\033[m')
valorhora = float(input('Digite o valor atual da sua hora trabalhada: '))
valorsalario = valorhora*220
print('Seu salario será de \033[34mR${:.2f}\033[m neste mês.'.format(valorsalario))
