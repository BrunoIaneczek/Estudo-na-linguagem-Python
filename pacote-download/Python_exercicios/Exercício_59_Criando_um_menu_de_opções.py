# Crie um programa que leia dois valores e mostre em menu na tela
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos numeros
# [5] sair do programa
print(20*'=','\033[34mCALCULADOR ENTRE DOIS NÚMEROS\033[m',20*'=')
print(15*'=','\033[36mMENU DE OPÇÕES\033[m',15*'=')
print('[1] somar')
print('[2] multiplicar')
print('[3] maior')
print('[4] novos numeros')
print('[5] sair do programa')
print(55*'==')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro numero: '))
opcao = 0
while opcao !=5:
    opcao = int(input('\033[36mDigite a opção da operação que deseja realizar:\033[m '))
    if opcao == 1:
        s = n1+n2
        print('A soma deste numeros é \033[34m{}.\033[m'.format(s))
        print(50*'==')
    elif opcao == 2:
        m = n1*n2
        print('O resultado da multiplicação entre estes dois numeros é \033[31m{}.\033[m'.format(m))
        print(50 * '==')
    elif opcao == 3:
        if n1 != n2:
            maior = max(n1,n2)
            print('O maior numero entre os 2 numeros digitados é \033[33m{}.\033[m'.format(maior))
        else:
            print('Ambos numeros são iguais.')
        print(50 * '==')
    elif opcao == 4:
        n1 = int(input('Digite novo número: '))
        n2 = int(input('Digite segundo novo numero: '))
    elif opcao == 5:
        print('\033[31mPrograma encerrado.\033[m')
    else:
        print('Opção inválida, digite uma opção válida.')
print('Volte sempre, obrigado')

