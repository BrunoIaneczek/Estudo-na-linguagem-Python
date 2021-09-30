'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores
podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;'''
resp =''
while True:
    a = float(input('Digite a medida do primeiro lado: '))
    b = float(input('Digite a medida do segundo lado: '))
    c = float(input('Digite a medida do terceiro lado: '))
    if ( b - c ) < a < b + c or ( a - c ) < b < a + c or ( a - b ) < c < a + b:
        print('Pode se fazer um triangulo')
        if a == b == c:
            print('Triangulo equilatero')
        elif a == b != c or a==c != a or b==a != c:
            print('Triangulo isoceles')
        elif a != b != c:
            print('Triangulo escaleno')
    else:
        print('Nao se pode fazer um triangulo')
    resp = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    while resp not in 'sn':
        resp = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if resp == 'n':
        break
print('programa encerrado')