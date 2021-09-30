'''Faça um Programa que leia três números e mostre-os em ordem decrescente'''


n1=n2=n3=0
op=''
while op in 's':
    n1 = int(input('Digite o primeiro numero: '))
    n2 = int(input('Digite o segundo numero: '))
    n3 = int(input('Digite o terceiro numero '))
    lista = (n1,n2,n3)
    maior = max(lista)
    menor = min(lista)
    if n1 < maior and n1 > menor:
        print(maior,n1,menor)
    if n2 < maior and n2 > menor:
        print(maior,n2,menor)
    if n3 < maior and n3 > menor:
        print(maior,n3,menor)
    op = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
print('encerrado')