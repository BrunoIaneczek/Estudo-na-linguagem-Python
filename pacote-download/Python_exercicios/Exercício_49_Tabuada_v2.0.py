# refaça o exercicio 9 agora utilizando laços

n = int(input('Digite um numero para ver sua tabuada: '))
for c in range(1,11):
    print(n,'x',c, '= {}'.format(c*n))