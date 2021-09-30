'''num = [1,2,3,4,5]
num[2]=9
num.append(6)
num.sort()
num.insert(2,4)
num.remove(4) # se houver elementos repetidos, ele removera o primeiro elemento a aparecer na lista
num.pop()
if 6 in num:
    num.remove(6)
else:
    print('Não existe na lista 99')
#num.sort(reverse=True)
print(num)
print(f'Esta lista tem {len(num)} elementos.')'''

valores = []
for cont in range(0,5):
    valores.append(int(input("Digite um valor")))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('cheguei ao fim dalista')

a = [1,2,3,4]
b = a[:] #Desta forma se copia uma lista
b[2]=5
print(a)
print(b)

