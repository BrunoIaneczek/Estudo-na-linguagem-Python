'''Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
 Dica: utilize o operador módulo (resto da divisão).'''

resp = ''
while resp != 'n':

    num = int(input('Digite um numero: '))
    valor = num%2
    if valor == 0:
        print('O numero e par!')
    else:
        print('O numero e impar!')
    resp = input('Deseja continuar?[S/N] ')
print('Programa encerrado com sucesso!')
