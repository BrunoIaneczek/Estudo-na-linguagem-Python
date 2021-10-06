
precos = [0,4.00,4.50,5.00,2.00,1.50]
codigo, quantidade = input().split(' ')
valor = precos[int(codigo)] * float(quantidade)
print(f'Total: R$ {valor:.2f}')
