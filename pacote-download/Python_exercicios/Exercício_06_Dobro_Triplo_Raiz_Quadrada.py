#Crie um algoratimo que leia um número e mostre seu dobro,triplo e raiz quadrada.

num = int(input('digite um valor: '))
dobro = num*2
triplo = num*3
raiz = num**(1/2)
print('o dobro de {} é {}.'.format(num, dobro))
print('o triplo de {} é {}.'.format(num, triplo))
print('a raiz quadrada de {} é {}.'.format(num, raiz))