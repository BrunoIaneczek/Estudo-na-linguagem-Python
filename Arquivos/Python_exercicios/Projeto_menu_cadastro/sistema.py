from formatacao import *
from funcaodeArquivo import *
arq = 'lista'
if not arquivoexiste('lista'):
    criandoarquivo('lista')

titulo1('Sistema de cadastro')
espaco('', 2)
menu = '''
Opção 1 - Cadastrar pessoa
Opção 2 - Listar pessoas
Opção 3 - Sair'''
while True:
    try:
        titulo2('MENU')
        print(menu)
        espaco('', 1)
        opcao = int(input('Digite a opção desejada: '))
        while opcao > 3:
            opcao = int(input(fonteazul('Opção inválida, digite novamente: ')))

        if opcao == 1:
            nome = str(input('Nome: '))
            idade = seinteiro('Idade: ')
            cadastrar(arq,nome,idade)

        elif opcao == 2:
            verarquivo('lista')

        else:
            break

    except:
        fontevermaelha('ERRO! O VALOR DIGITADO ESTA FORA DOS PARAMETROS.')
