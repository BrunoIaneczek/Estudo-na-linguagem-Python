valor = float(input('Digite o valor '))
n100 = 100
n50 = 50
n20 = 20
n10 = 10
n5 = 5
n2 = 2
m1 = 1
m050 = 0.50
m025 = 0.25
m010 = 0.10
m005 = 0.05
m001 = 0.01
qtd100 = 0
qtd50 = 0
qtd20 = 0
qtd10 = 0
qtd5 = 0
qtd2 = 0
qtd1 = 0
qtd050 = 0
qtd025 = 0
qtd010 = 0
qtd005 = 0
qtd001 = 0

while valor >=100:
        valor = valor-n100
        qtd100+=1
while valor >=50:
        valor = valor-n50
        qtd50+=1
while valor>= n20:
        valor = valor-n20
        qtd20+=1
while valor >= n10:
        valor = valor-n10
        qtd10+=1
while valor >= n5:
    valor = valor-n5
    qtd5+=1
while valor >= n2:
    valor = valor-n2
    qtd2+=1
while valor >=m1:
    valor = valor-m1
    qtd1+=1
while valor >= m050:
    valor = valor-m050
    qtd050+=1

print(valor,qtd100,qtd50,qtd20,qtd10,qtd5,qtd2,qtd1,qtd050)

    
