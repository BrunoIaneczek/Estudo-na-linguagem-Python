'''faça um programa que, dado um conjunto de N números,
 determine o menor valor, o maior valor e a soma dos valores'''

lista = [12,34,2,45,6,7,23]
maior = lista[0]
menor = lista[0]
s = 0
for valor in lista:
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
    s+=valor
#print(maior)
print(menor)
print(maior)
print(s)

i = 0
while i < len(lista):
    if lista[i]> maior:
        maior = lista[i]
    if lista[i] < menor:
        menor = lista[i]
    i+=1
print(maior)
print(menor)








