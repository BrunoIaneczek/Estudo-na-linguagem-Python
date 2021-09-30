# COMANDOS PARA TRAAMENTO

'''try:
    operação( aqui se encontrara, o código)
except:
    se falhou( aqui se o codigo der erro , retornara algo, uma msg por exemplo)

else:
    se deu certo ( aqui se o código esta correto, seguira normalmente)
finally:
    se der errado/certo ( aqui independente se o codigo estiver correto ou errado ele retornara o que se quer'''

# exemplo
'''try:
    a = int(input('Digite numerador: '))
    b = int(input('Digite denominador: '))
    r = a / b
except Exception as erro:
    print(f'Infelizmente ocorreu o erro {erro.__class__}') # Utilizando o Excepetion podemos saber causa, tipo de erro etc
#except:
#    print('Infelizmente houve um erro')
else:
    print(f'O valor do resultado é {r:.1f}')
finally:
    print('Programa encerrado')'''

# DEFININDO AÇOES PARA DIVERSOS TIPOS DE ERRO

try:
    a = int(input('Digite numerador: '))
    b = int(input('Digite denominador: '))
    r = a / b
except (ValueError,TypeError):
    print('Obtemos erro com os dados informados')
except (ZeroDivisionError):
    print('Um dos dados informados e 0, não sendo possivel a divisão')
except (KeyboardInterrupt):
    print('Não foi informado um, ou mais dados necessários')
else:
    print(f'O valor do resultado é {r:.1f}')
finally:
    print('Programa encerrado')
