salario = float(input())'''

# Taxas de imposto
if salario >= 0.00 and salario <= 2000.01:
    taxa = 0
elif salario >= 2000.01 and salario <= 3000.00:
     dif = salario-2000.01
     taxadif = 8
     taxa = 0
elif salario >= 3000.01 and salario <= 4500.00:
    dif = salario - 3000.01
    taxa = 8
    taxadif = 18
elif salario >= 4500:
    taxa = 28

for i in range(4):
'''


lista = []
for i in range(0,2001):
    lista.append(i)
if salario in lista:


