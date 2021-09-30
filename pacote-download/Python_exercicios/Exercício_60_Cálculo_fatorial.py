n = int(input('Digite um numero para seu fatorial: '))
f = 1
print('{}! > '.format(n),end='')
for c in range(n,0,-1):
    print('{} X '.format(c),end='')
    f*=c
print('=',f)
