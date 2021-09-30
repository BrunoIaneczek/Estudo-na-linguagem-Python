#Estrutura de respetição while true e comando break

#999 é o flag

'''s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
print(f'A soma dos numeros é {s}') #fstring'''

nome = 'bruno'
sexo = 'masculino'
idade = 26
print(f'O {nome} tem {idade} anos e é do sexo {sexo}')

#fstrings exemplos
print(f'{nome:20}')
print(f'{nome:^20}')
print(f'{nome:-^20}')
print(f'{nome:->20}')
print(f'{nome:-<20}')
