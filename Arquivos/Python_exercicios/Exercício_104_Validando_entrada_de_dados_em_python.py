'''Crie um programa que tenha a função leiaint()
que vai funcionar semelhante a função input()
so que realizando a validação para aceitar somente um valor numerico'''

def leiaint(msg):
        valor = 0
        a = str(input(msg))
        while True:
                if a.isnumeric():
                        valor = int(a)
                        break
                else:
                        print('ERRO! Digite um numero inteiro válido')
                a = input("digite um numero: ")
        return valor


a = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o número {a}')







