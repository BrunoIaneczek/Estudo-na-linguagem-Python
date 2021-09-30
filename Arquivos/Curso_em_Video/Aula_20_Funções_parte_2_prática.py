# Fatorial
def fatorial(num = 1):
    f  =  1
    for c in range (num, 0 ,-1):
        f *= c
    return f
f1 = fatorial(6)
f2 = fatorial(5)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

# Retorno de valor lógico

def par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False


lista = []
num = 0
while num != 7:
    num = int(input('Digite um numero: '))
    lista.append(num)
for item in lista:
    if par(item):
        print(f'O {item} é par')
    else:
        print(f'O {item} é impar')

