'''lista = []
for x in range(0,5):
    n = int(input('Digite um número: '))
    lista.append(n)
a = max(lista)
b = min(lista)
lista.remove(max(lista))
lista.remove(min(lista))
c = max(lista)
d = min(lista)
lista.remove(max(lista))
lista.remove(min(lista))
e = lista[0]
print(f"Os valores digitados foram {b},{d},{e},{c},{a}.")'''

#Solução curso em video

lista = []
for c in range(0,5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                break
            pos+=1
print(lista)








