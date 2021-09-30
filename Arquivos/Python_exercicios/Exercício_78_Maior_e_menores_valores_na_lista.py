'''Faça um programa que leia 5 valores numéricos e guarde-os
em uma lista. No final, mostre qual foi o maior e o menor valor digitado
e mostre suas posiçoes'''

#minha resolução
valores = []
for v in range(0,5):
    valores.append(int(input('Digite um valor: ')))
print(f'O maior valor foi {max(valores)} nas posiçoes ',end='')
for c ,v in enumerate(valores):
    if v == max(valores):
        print(f' {c}...',end='')
print(f'\nO menor valor foi {min(valores)} nas posiçoes ',end='')
for c , v in enumerate(valores):
    if v == min(valores):
        print(f' {c}...',end='')

#resolução curso em video
mai = 0
min = 0
valores = []
for c in range (0,5):
    valores.append(int(input(f'Digite um valor para posição {c}: ')))
    if c == 0:
        c = min = mai = valores[c]
    else:
        if valores[c]>mai:
            mai = valores[c]
        if valores[c]< min:
            min = valores[c]
print(valores)
print(f'O maior valor digitado foi {mai} nas posiçoes ',end='')
for i, c in enumerate(valores):
    if c == mai:
        print(f'{i}...',end='')
print(f'\nO menor valor foi {min} nas posiçoes ',end='')
for i , c in enumerate(valores):
    if c == min:
        print(f'{i}...',end='')

