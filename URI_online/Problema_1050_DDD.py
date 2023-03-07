'''ddd = int(input(''))

if ddd == 61:
    print('Brasilia')
elif ddd == 71:
    print('Salvador')
elif ddd == 11:
    print('Sao Paulo')
elif ddd == 21:
    print('Rio de Janeiro')
elif ddd == 32:
    print('Juiz de Fora')
elif ddd == 19:
    print('Campinas')
elif ddd == 27:
    print('Vitoria')
elif ddd == 31:
    print('Belo Horizonte')
else:
    print('DDD nao cadastrado')
        '''

'''resposta = 's'
while resposta in 'Ss':
    nome_aluno = input("digite o nome do aluno: ")
    n1 = float(input('Digite a nota 1: '))
    n2 = float(input("Digite nota 2: "))
    media = (n1 + n2) / 2
    if media >= 6:
        print('aluno Aprovado')
    else:
        print('Aluno reprovado')
    resposta = input('Deseja informar dados de mais um aluno "S" ou "N": ')
    

'''
'''contador = 0
for i in range(0,5):
    nome = input("Nome:")
    idade = int(input('Idade: '))
    sexo = input('sexo: ')
    if sexo == 'f' and idade > 35:
        contador+=1
print(f'A quantidade de mulheres maiores de 35 é {contador}')
'''
acumulador=0
for i in range (0,3):
    salario = float(input('Salario: '))
    nome = input('Nome: ')
    acumulador+=salario

print(f'A soma dos salarios é de {acumulador}')