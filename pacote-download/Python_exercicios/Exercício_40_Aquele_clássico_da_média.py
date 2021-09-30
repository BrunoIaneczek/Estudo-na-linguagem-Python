# Crie um programa que leia 2 notas de um aluno e calcule sua média, mostrando uma mensagem no final
# De acordo com a média atingida.
# média abaixo de 5.0 reprovado
# média entre 5.0 e 6.9 recuperação
# média 7.0 ou superior aprovado.

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
média = (n1+n2)/2
if média < 5.0:
    print('Sua média foi5 \033[31m{}\033[m logo você está reprovado.'.format(média))
elif média>=5.0 and média<=6.9:
    print('Sua média foi \033[32m{}\033[m você está em recuperação.'.format(média))
else:
    print('Sua média foi \033[34m{}\033[m, parabéns você está aprovado.'.format(média))