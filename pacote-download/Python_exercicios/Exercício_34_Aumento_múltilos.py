#  Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a  R$1.250,00, calcule um aumento de 10%.
# Para inferiores ou iguais, o aumento é de 15%.


salário = float(input('Digite o valor do salário do funcionário: R$'))
a = (salário*10)/100
b = (salário*15)/100
if salário <= 1250:
    print('O aumento será de \033[31mR${:.2f}\033[m e o novo salário será de \033[33mR${:.2f}\033[m.'.format(b, salário+b))
else:
    print('O aumento será de \033[32mR${:.2f}\033[m e o novo salário será de \033[34mR${:.2f}\033[m.'.format(a, a+salário))