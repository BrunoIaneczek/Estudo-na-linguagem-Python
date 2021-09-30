'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16'''

while True:
    resp = ''
    num = int(input('Digite um numero menor que 1000: '))
    centenas = num//100
    a = centenas*100
    b = num-a
    dezenas = b//10
    c = dezenas*10
    d = b-c
    unidades = d//1
    if centenas == 0 and dezenas != 0:
        print(f'{num} = {dezenas} dezenas e {unidades} unidades.')
    elif dezenas == 0 and unidades !=0:
        print(f'{num} = {unidades} unidades.')
    elif centenas != 0:
        print(f'{num} = {centenas} centenas, {dezenas} dezenas e {unidades} unidades.')
    print('')
    resp = str(input('Deseja continuar [S/N]? ')).strip().lower()[0]
    while resp not in 'sn':
        resp = str(input('Deseja continuar [S/N]? ')).strip().lower()[0]
    if resp == 'n':
        break
print('Programa encerrado!')


