from time import sleep
lista = []
dados = []
while True:
    dados.append(str(input('Digite o nome do aluno: ')).strip())
    dados.append(float(input('Digite o valor da nota1: ')))
    dados.append(float(input('Digite o valor da nota2: ')))
    lista.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N]? ')).upper()
    while resp not in 'SN':
        resp = str(input('Digite sim ou não [S/N]: ')).upper()
    if resp == 'N':
        break
print(20*'-=-')
print('Nº aluno  média')
for a, i in enumerate(lista):
    media = (i[1] + i[2]) / 2
    print(f'{a}  {i[0]:^5}     {media:^5}')
print(20*'-=-')
while True:
    notas = int(input('Mostrar notas de qual aluno (999)interrompe: '))
    if notas == 999:
        print('Finalizando...')
        sleep(1)
        print('Fim do programa')
        break
    if notas <= len(lista) -1: #linha que peguei do cód guanabara
        print(f'As notas de {lista[notas][0]} foram {lista[notas][1]} e {lista[notas][2]}')
        print(20 * '-=-')
