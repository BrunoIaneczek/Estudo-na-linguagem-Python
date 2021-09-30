# Desenvolva um programa que leia 6 numeros inteiros
# e mostre a soma somente daqueles que forem pares
# se o valor digitado for impar desconsidere_-o
soma = 0
for c in range(0, 6):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma+=num
print(soma)

soma = 0
cont = 0
for c in range(1,6):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 3 == 0 and not num % 2 == 0:
        soma+= num
        cont+=1
print(soma,cont)
