frase = (str(input('Digite uma frase: ')).strip())
x = frase.count(' ')
y = len(frase)
z = y - x
c = 0
for letra in range(0, y):
    print(frase[letra])
print(10 * '=')
for letra in range(0, y+1):
    print(frase[letra-1])
