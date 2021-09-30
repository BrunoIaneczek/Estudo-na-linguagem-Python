# Modularização em python

'''VANTAGENS

* ORGANIZAÇÃO DO CÓDIGO

* FACILIDADE DE MANUTENÇÃO

* OCULTAÇÃO DE CÓDIGO DETALHADO

* REUTILIZAÇÃO EM OUTROS PROJETOS'''

'''Para se utilizar de modulos se cria um arquivo com as funções
e quando se quiser usar das mesmas se importa deste arquivo as funçoes para determindado 
programa exemplo
Arquivo: uteis
(import uteis)'''

def fatorial(n):
    f=1
    for c in range(1,n+1):
        f*=c
    return f


num=int(input("Digite um valor "))
fat=fatorial(num)
print(f"O fatorial de {num} é {fat}")