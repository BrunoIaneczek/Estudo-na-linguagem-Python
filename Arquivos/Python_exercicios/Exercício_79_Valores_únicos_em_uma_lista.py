'''Crie um programa onde o usuário possa digitar vários
valores e cadastre-os em uma lista.Caso o número ja exista na lista
não será adicionado. No final serão exibidos todos os valores únicos
digitados, em ordem crescente'''

lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor  adicionado.')
    else:
        print('Valor não adicionado.')
    resp = str(input('Você deseja continuar?[S/N] '))
    if resp in 'Nn':
        break
    while resp not in 'SsnN':
        resp = str(input('Resposta inválida, tente novamente: '))
lista.sort()
print(lista)

