idade = int(input())
anos = idade // 365
r = idade % 365

meses = r//30
r = r % 30

dias = r//1
r = r % 1

print(anos, 'ano(s)')
print(meses, 'mes(es)')
print(dias, 'dia(s)')
