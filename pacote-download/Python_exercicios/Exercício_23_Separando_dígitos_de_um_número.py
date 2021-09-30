# faça um programa que leia u numero de 0 a 9999e mostre na tela cada um dos digitos separados.
#ex: digitie um numero: 1834
# unidade: 4, dezena:3, centena:8, milhar:1

#metodo usando string

num = int(input('Digite um numero entre 0 e 9999: '))
dnum = str(num)
#enum = ' '.join(num) nao é nescesario estas funçoes so a conversao pra string mas tbm esta correto
#print(enum)
#dnum = enum.split()
#print('unidade:{} '.format(dnum[3]))
#print('dezena:{}'.format(dnum[2]))
#print('centena:{}'.format(dnum[1]))
#print('milhar: {}'.format(dnum[0]))

#metodo matematico

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena:{}'.format(c))
print('milhar:{}'.format(m))