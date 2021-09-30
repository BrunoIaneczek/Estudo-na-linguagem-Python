# cores no terminal

print('\033[0;30;41mteste\033[m')
print('\033[4;33;44mteste\033[m')
print('\033[0;35;43mteste\033[m')
print('\033[0;30;42mteste\033[m')
print('\033[0;30;0mteste\033[m')
print('\033[7;30mteste\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[34m{}\033[m!!!'.format(a , b))

nome = 'Bruno'
print('Olá muito prazer em te conhecer, {}{}{}!!'.format('\033[4;34m',nome,'\033[m'))