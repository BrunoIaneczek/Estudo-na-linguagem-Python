'''Desenvolva um programa que leia quatro valores
pelo teclado e guarde-os em uma tupla.No final, mostre:
A) Quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro 3
C) Quais foram os números pares'''

valores = (int(input('Digite um valor: ')),int(input('Digite um valor: ')),
           int(input('Digite um valor: ')),int(input('Digite um valor: ')))
print('')
print(f'Você digitou os numeros {valores}.')
print(f'O número 9 apareceu {valores.count(9)} vezes na lista.')
if 3 in valores:
    print(f'O numero 3 aparece primeiro na posição {valores.index(3)+1}ª')
else:
    print('O numero 3 nao foi digitado em nenhuma posição.')
print('Os numeros pares digitados foram',end=' ')
for n in valores:
    if n % 2 == 0:
        print(n,end=' ')