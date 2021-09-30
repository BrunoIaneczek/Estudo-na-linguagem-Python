

""" Criando um Menu de Opções """

# importações de Bibliotecas
import color
from time import sleep

# Variaveis
Menu = 0

valor1 = 0
valor2 = 0
# Estrutura de Repetição
while Menu != 5:
    print('{} Menu De Operações {}'.format(color.blue('=*=' * 15), color.blue('=*=' * 15)))

    # Entrada de valor Usuario
    if Menu == 0 or Menu == 4:
        valor1 = int(input(color.yellow('Digite um Valor:')))
        valor2 = int(input(color.yellow('Digite Outro Valor:')))

    Menu = int(input(color.magenta(""" Informe Qual Operação Deseja
    [1] Somar Valores
    [2] Multiplicar Valores
    [3] Maior Valor
    [4] Solicite Novos moedas
    [5] Para Sair:""")))
    print(color.blue('=*=' * 36))

    # Estrutura de decisão para Adição
    if Menu == 1:
        soma = valor1 + valor2
        print("""{}
            A soma Resultou em : {} + {} = {}""".format(color.yellow('O Resultado Da Operação'), valor1, valor2,
                                                        color.red(soma)))
    # Estrutura de decisão Para Multiplicação
    elif Menu == 2:
        Multiplicar = valor1 * valor2
        print("""{}
            A multiplicação Resultou: {} x {} = {}""".format(color.yellow('O Resultado Da Operação'),
                                                             valor1, valor2, color.red(Multiplicar)))

    # Maior Numero
    elif Menu == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print("""{}
            O Maior Valor Digitado entre:{} e {} foi {}""".format(color.yellow('O Resultado Da Operação'),
                                                                  valor1, valor2, color.red(maior)))

    # Novos moedas
    elif Menu == 4:
        Menu = 4

    # Sair Do Menu
    elif Menu == 5:
        Menu = 5
        print(color.red('FINALIZANDO..'))
        sleep(0.6)
        print(color.blue('=-=-=-= ATE A PROXIMA <3 =-=-=-='))
    else:
        print(color.red('{}Opção Invalida.  Verifique sua Opção '.format(' ' * 35)))

