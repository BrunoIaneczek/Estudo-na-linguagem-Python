'''Altere o programa anterior para mostrar no final a soma dos números.'''
num1 = int(input('Digite o primeiro numero do intervalo: '))
num2 = int(input('Digite o segundo numero do intervalo: '))
s = 0
for c in range(num1+1 , num2):
    print(c, end=' ')
    s+=c
print()
print(f'A soma entre os numeros no intervalo é de {s}.')