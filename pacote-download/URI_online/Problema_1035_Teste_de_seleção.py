'''A, B, C, D = input().split(" ")
A = int(A)
B = int(B)
C = int(C)
D = int(D)

if B > C:
    ver1 = 1
else:
    ver1 = 0

if D > A:
    ver2 = 1
else:
    ver2 = 0

somacd = C+D
somaab = A+B

if somacd > somaab:
    ver3 = 1
else:
    ver3 = 0

if C > 0 and D > 0:
    ver4 = 1
else:
    ver4 = 0

if A % 2 == 0:
    ver5 = 1
else:
    ver5 = 0

somaver = ver1+ver2+ver3+ver4+ver5

if somaver == 5:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')'''




print('Bem-vindo(a)! Para abrir uma conta corrente responda às seguintes perguntas: ')

p1 = input('Você tem em mãos o documento de identidade, sim ou não?')
p2 = input('Você tem em mãos um comprovante de residência, sim ou não? ')

if p1 == 'não' or p2 == 'não':
    print('Sinto muito, você não tem os documentos necessários para a abertura de conta corrente.')
else:
    print('Certo. Vamos prosseguir com a abertura da sua conta corrente.')