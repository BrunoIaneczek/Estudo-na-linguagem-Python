'''teste = list()
teste.append('Bruno')
teste.append('26')
galera = list()
galera.append(teste[:])
teste[0] = 'Larissa'
teste[1] = 23
galera.append(teste[:])
print(galera)
print('\033[34mparte 1\033[m')

pessoas = [['joao',19],['ana',33],['joaquim',13],['maria',45]]
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print('\033[31mparte 2\033[m')
for pessoa in pessoas:
    #print(pessoa) #conteudo total sublista
    #print(pessoa[0]) #conteudo selecionado da sublista, nome neste caso
    #print(pessoa[1]) #conteudo selecionado da sublista, neste caso idade
    print(f'{pessoa[0]} tem {pessoa[1]} anos.')'''
print('\033[33mparte 3\033[m')
gente = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome ')))
    dado.append(int(input('idade ')))
    gente.append(dado[:])
    dado.clear()
print(gente)
print('\033[35mparte 4\033[m')
totam=totamen=0
for pessoa in gente:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade')
        totam+=1
    else:
        print(f'{pessoa[0]} é menor de idade')
        totamen+=1
print(f'Existem {totam} maiores de idade e {totamen} menores de idade')