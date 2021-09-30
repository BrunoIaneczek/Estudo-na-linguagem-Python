'''Faça um programa que peça dois números, base e expoente,
calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.'''


def potencia(num1,num2):
    m = 1
    for c in range(0,num2):
        m*=num1
    print(f'O valor {num1} elevado ao expoente {num2} é igual a {m}.')

potencia(2,6)
valor1 = int(input('Digite o número base: '))
valor2 = int(input('Digite o número expoente: '))
potencia(valor1,valor2)

