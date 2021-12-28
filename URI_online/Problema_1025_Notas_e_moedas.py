valor = float(input())

#Valores notas
n100 = 100
n50 = 50    
n20 = 20
n10 = 10
n5 = 5
n2 = 2

#Valores moedas
m1 = 1
m050 = 0.50
m025 = 0.25
m010 = 0.10
m005 = 0.05
m001 = 0.01

#Quantidade notas
qtd100 = 0
qtd50 = 0
qtd20 = 0
qtd10 = 0
qtd5 = 0
qtd2 = 0

#Quantidades moedas
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
while valor >= m025:
        valor = valor - m025
        qtd025+=1
while valor >= m010:
        valor = valor - m010
        qtd010+=1
while valor >= m005:
        valor = valor-m005
        qtd005+=1
while valor >= m001:
        valor =  valor - m001
        qtd001+=1

print(f'''
NOTAS:
{qtd100} nota(s) de R$ {n100:.2f}
{qtd50} nota(s) de R$ {n50:.2f}
{qtd20} nota(s) de R$ {n20:.2f}
{qtd10} nota(s) de R$ {n10:.2f}
{qtd5} nota(s) de R$ {n5:.2f}
{qtd2} nota(s) de R$ {n2:.2f}
MOEDAS:
{qtd1} moeda(s) de R$ {m1:.2f}
{qtd050} moeda(s) de R$ {m050:.2f}
{qtd025} moeda(s) de R$ {m025}
{qtd010} moeda(s) de R$ {m010:.2f}
{qtd005} moeda(s) de R$ {m005}
{qtd001} moeda(s) de R$ {m001}
''')


    
