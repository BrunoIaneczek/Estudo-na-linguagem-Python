impares = []
pares = []
lista = []
for c in range(1,8):
    n = (int(input(f'Digite o {c}º valor: ')))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
lista.append(pares[:])
lista.append(impares[:])
pares.clear()
impares.clear()
lista[0].sort()
lista[1].sort()
print(30*'\033[34m-=-\033[m')
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')

