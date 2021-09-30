# Refaça o exercicio 28 agora utilizando while, e um numero entre 0 e 10.
from random import randint
pc = randint(0,10)


usern = 0
palpites = 0
while usern != pc:
    usern = int(input('Qual e o seu palpite? '))
    if usern > pc:
        print('menos...Você nao acertou tente novamente.')
    elif usern == pc:
        print('Você acertou!!')
    else:
        print('mais...Você nao acertou tente novamente.')
    palpites +=1
print(30*'\033[31m==\033[m'),print('\033[36mPARABÊNSSS!!!\033[m'),print(30*'\033[31m==\033[m')
print('O número era \033[33m{}\033[m e numero de palpites foi de \033[34m{}\033[m.'.format(usern,palpites))
