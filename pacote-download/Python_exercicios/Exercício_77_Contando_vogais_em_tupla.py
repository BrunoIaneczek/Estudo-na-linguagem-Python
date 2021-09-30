'''Crie um programa que tenha uma tupla com várias palavras
 Depois disso, você deve mostrar, para cada palavra,quais são as suas vogais'''

# METODO QUE UTILIZEI
palavras = ('atum','batata','pao','carne','geleia','ovo')
for a in range(0,len(palavras)):
    palavra = palavras[a]
    print(f'\nA palavra {palavra} tem as vogais  ',end='')
    for c in range(0,len(palavra)):
        if (palavra[c]) in ('a','e','i','o','u'):
            print(palavra[c],end=' ')
print('')
print('')
# MELHOR METODO
for p in palavras:
    print(f'\nA palavra \033[34m{p.upper()}\033[m tem as seguintes vogais  ',end='')
    for letra in p:
        if letra in 'aeiou':
            print(f'{letra}',end=' ')







