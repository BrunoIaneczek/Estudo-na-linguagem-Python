num = 0
s = 0
c = 0
while num != 999:
    num = int(input('Digite um número: '))
    c += 1
    s = s+num
    
print(f'A soma dos números é {s-999}')
print(f'E foram digitados {c-1} números')
