'''Melhore o execicio 61, perguntando para  usuário se ele quer mostrar
 mais alguns termos. O programa encerra quando ele disser que quer mostar 0 termos'''

n = int(input('Digite o numero que será o primeiro da PA: '))
r = int(input('Digite a razão da PA: '))
termo = n
c = 0
s = 0
termos = 1
while termos != 0:
    while c <= 10:
        termo = termo + r
        c+=1
        print(termo,end=' > ')
    d = 0
    termos = int(input('\nquantos termos quer a mais: '))
    while d <= termos-1:
        termo = termo + r
        d += 1
        print(termo,' > ' ,end='')
    s+=termos
    tt=(s+10)
print('Progressão encerrada com {} termos. '.format(tt))












