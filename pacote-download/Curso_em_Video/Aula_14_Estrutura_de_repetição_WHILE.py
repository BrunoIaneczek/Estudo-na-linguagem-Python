# Estrutura while
# Diferente do For o while roda deteminada informaçao infinitamente ate que ocorra algum evento, que
# pare o programa.

'''enquanto não maça
    se chão
        passo
    se buraco
        pula
    se moeda
        pega
pega'''

'''while not maça:
    if chão:
        passo
    if buraco:
        pula
    if moeda:
        pega
pega'''

# Exemplos

'''c = 1
while c<10:
    print(c)
    c+=1
print('fim')'''

'''n = 1
while n != 0:
    n = int(input('Digite um numero: '))
print('FIM!!')'''

r = 's'
while r == 's':
    n = int(input('Digite um numero: '))
    r = str(input('Você quer continuar [S/N]? ')).strip().lower()
print('\033[34mFIM!!!\033[m')



