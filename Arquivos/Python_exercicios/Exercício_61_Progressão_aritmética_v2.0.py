'''Refaça o exercicio 51 agora utilizando  while'''

'''n = int(input('Digite o primeiro termo da PA: '))
r= int(input('Digite a razão da PA: '))
c = n-r
print('A PA de \033[36m{}\033[m é:'.format(n))
while c < (n + (10-1)*r):
    c = c+r
    c+=0
    print(c,'> 'if c < (n + (10-1)*r) else '\033[31mAcabou.\033[m',end='')'''

n = int(input('Digite o primeiro termo da PA: '))
r= int(input('Digite a razão da PA: '))
termo = n-r
c = 0
while c <= 10:
    termo = termo + r
    print(termo,'> ' if c < 10 else '.',end='')
    c+=1

