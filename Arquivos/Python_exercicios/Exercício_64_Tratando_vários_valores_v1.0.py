'''Crie um programa que leia vários numeros inteiros, o programa só vai parar
quando o usuário digitar o valor 999, no final mostre quantos numeros foram digitados e qual foi a soma entre eles
descosiderando o flag(999)'''
'''Minha solução'''
num = count = soma = 0
while num != 999:
    num = int(input('Digite um numero inteiro [999 para parar]: '))
    count += 1
    c = count-1
    soma = num+soma
    s = soma-999
print('Foram digitados \033[34m{}\033[m numeros e a soma entre eles é \033[31m{}\033[m.'.format(c, s))

'''Solução curso em video'''
num = count = soma = 0
num = int(input('Digite um numero [999 pra parar] '))
while num != 999:
    count+=1
    soma+=num
    num = int(input('Digite um numero [999 pra parar] '))
print('Você digitou {} numeros e a soma entre eles é {}.'.format(count,soma))