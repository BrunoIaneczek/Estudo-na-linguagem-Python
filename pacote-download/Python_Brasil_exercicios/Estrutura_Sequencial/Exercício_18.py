'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)'''

print(10*'==','\033[31mPrograma para calcular tempo de download\033[m',10*'==')
print(' ')
opcao = 's'
arquivo = velocidade = 0
while opcao in 'Ss':
    arquivo = float(input('Digite o tamanho do arquivo em (MB): '))
    velocidade = float(input('Digite a velocidade do link em (Mbps): '))
    tempo = arquivo/(velocidade/8)
    tempomin = tempo/60
    if tempo > 60:
        print('O download levara cerca de \033[36m{:.2f}\033[m min.'.format(tempomin))
    else:
        print('O download levara cerca de \033[32m{:.2f}\033[m sec.'.format(tempo))
    print(' ')
    opcao = str(input('Deseja continuar [S/N]: ')).strip().lower()[0]
print('Encerrado')
