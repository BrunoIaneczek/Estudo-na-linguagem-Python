'''Crie um programa que vai ler vários números e colocar em uma lista
Depois disso, crie duas listas extras que vão coter apenas
os valores pares e os valores impares digitados, ao final
mostre o conteudo das três lista geradas..'''

lista = []
lista2 = []
lista3 = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar [S/N]? ')).strip().lower()
    while resp not in 'SsNn':
        resp = str(input('Resposta inválida '))
    if resp in 'nN':
        break
for n in range(0,len(lista)):
    if lista[n] % 2 == 0:
        lista2.append(lista[n])
    else:
        lista3.append(lista[n])
print(f'A lista completa é \033[34m{lista}\033[m.')
print(f'A lista de números pares é \033[34m{lista2}\033[m')
print(f'A lista de números ímpares é \033[33m{lista3}\033[m')