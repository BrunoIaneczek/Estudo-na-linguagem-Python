lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
dados = []
linha2 = []
coluna3 = []
for linha in range(0, 3):
    for coluna in range(0, 3):
        lista[linha][coluna] = int(input(f'Digite um numero para posição [{linha},{coluna}] '))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{lista[linha][coluna]:^5}]', end='')
    print()
for sub in lista:
    for num in sub:
        dados.append(num)
s = 0
for c in dados:
    if c % 2 == 0:
        s = s + c
for l2 in lista[1]:
    linha2.append(l2)
s3 = 0
for i in range(0, 3):
    coluna3.append(lista[i][2])
    s3 = s3 + lista[i][2]

print(f'A soma dos valores pares é {s}.')
print(f'A soma dos valores da terceria coluna é {s3}.')
print(f'O maior valor da segunda linha é {max(linha2)}.')
