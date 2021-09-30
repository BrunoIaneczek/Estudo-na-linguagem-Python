from formatacao import *


# Função que válida um numero como inteiro
def seinteiro(msg):
    while True:
        try:
            idade = int(input(msg))
        except:
            print(fontevermaelha('ERRO! COLOQUE UM VALOR CORRETO!'))
        else:
            return idade


# Função que cria o arquivo
def criandoarquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro de criação')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


# Função que verifica se o arquivo já existe
def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


# Função que cadastra nova informação  no arquivo
def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print(fontevermaelha('Erro na abertura do arquivo!'))
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print(fontevermaelha('Erro ao escrever dados!'))
        else:
            print(fonteazul(f'Novo registro de {nome} adicionado com sucesso!'))
            espaco('', 1)
            a.close()


# Função que revela conteudo do arquivo
def verarquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        print(fontevermaelha(fontevermaelha('Erro ao ler arquivo!')))
    else:
        titulo3('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

    finally:
        a.close()
