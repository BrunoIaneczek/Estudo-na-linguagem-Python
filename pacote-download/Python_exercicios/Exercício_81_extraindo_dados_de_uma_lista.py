'''Crie um programa que vai ler vários números e colocar em uma lista
depois mostre:
A) Quantos numeros foram digitados.
B) A lista de valores em ordem decrescente.
C) Se o valor 5 foi encontrado na lista'''

lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? \033[33m[S/N]\033[m ')).strip().lower()
    while resp not in 'SsNn':
        resp = str(input('Opção incorreta! digite novamente \033[34m[S/N]\033[m: '))
    if resp in 'Nn':
        break
lista.sort(reverse = True)
print(30*'\033[34m-=-\033[m')
print(f'Foram digitados \033[36m{len(lista)}\033[m números.')
print(f'Os valores da lista em ordem decrescente são {lista}.')
if 5 in lista:
    print('O número 5 se encontra na lista.')
else:
    print('O número 5 não se encontra na lista.')

