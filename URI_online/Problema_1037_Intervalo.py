num = float(input())
intervalos = {"intervalo 0, 25":range(0,25000),'intervalo 25, 50':range(25000,50000),'intervalo 50, 75':range(50000,75000),'intervalo 75, 100':range(75000,100000)}

for k , v in intervalos.items():
    if num in v:
        print(f'{k}')
    else:
        print('Fora do intervalo')
        break