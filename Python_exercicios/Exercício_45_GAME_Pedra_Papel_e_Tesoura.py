from random import randint
from time import  sleep
pc = randint(1,3)
print(20*'*','JOGO PEDRA PAPEL E TESOURA',20*'*')
print('OPÇÕES')
print("""[1]PAPEL
[2]TESOURA
[3]PEDRA""")
user = int(input('Escolha sua jogada '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print(50*'-=-')
if pc == 1 and user == 1:
    print('Ambos escolheram papel, jogue novamente')
elif pc == 1 and user == 2:
    print('Você ganhou, tesoura vence papel')
elif pc == 1 and user == 3:
    print('Você perdeu, papel vence pedra')
elif pc == 2 and user == 1:
    print('Você perdeu, tesoura vence papel')
elif pc == 2 and user == 2:
    print('Ambos escolheram tesoura, jogue novamente')
elif pc==2 and user == 3:
    print('Você ganhou, pedra ganha de tesoura')
elif pc==3 and user ==1:
    print('Você ganhou. pedra perde pra papel')
elif pc==3 and user ==2:
    print('Você perdeu, pedra ganha de tesoura')
elif pc==3 and user==3:
    print('Ambos jogaram pedra, jogue novamente')
else:
    print('escolha inválida, faça sua escolha conforme opções acima')
print(50*'-=-')

