'''Crie um programa onde o usúario
digite uma expressão qualquer que use parênteses.Seu
aplicativo deverá analisar se a expressão passada está com
os parênteses abertos e fechados na ordem correta'''
lista = []
expressao = (str(input('Digite uma expressão ')))
for simb in expressao:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista)>0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressão válida')
else:
    print('Expressão invalida')