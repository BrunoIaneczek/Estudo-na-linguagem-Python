idade = int(input())
dias = 365
cont = 0
while True:
    if idade >= dias:
        idade -= dias
        cont += 1
    else:
        if dias == 365:
            dias = 30
            if cont > 0:
                print(f'{cont} ano(s)')
        elif dias == 30:
            dias = 1
            if cont > 0:
                print(f'{cont} mes(es)')
        elif dias == 1:
            dias = 0
            if cont > 0:
                print(f'{cont} dia(s)')
        cont = 0
        if idade == 0:
            break
