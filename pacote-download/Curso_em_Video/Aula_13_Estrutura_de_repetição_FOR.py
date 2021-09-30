 #ESTRUTURAS DE REPETIÇÃO

# laço c no intervalo(1,10)

#for c in range(1,10):
  #  passo
   # pula

#for c in range(1,10): #estrutura de laço simples
    #passo
    #pula
#passo
#pula

#for c in range(1,10):
#    if moeda:
#        pega
 #   passo
  #  pula
#passo
#pega

for c in range(0,7):
    print('oi')
print('fim')

#contagem regressiva
for c in range(6,0,-1):
    print(c)
print('fim')

#pulando variaveis
for c in range(0,52,2):
    print(c)
print('fim')

n= int(input('Digite um numero para ver os numeros anteriores '))
for c in range(0,n+1):
    print(c)
print('fim')

#com multiplas variaveis

i=int(input('Inicio: '))
p=int(input('passo:' ))
f=int(input('fim: '))
for c in range(i,f+10,p):
    print(c)
print('fim')

for c in range(0,3):
    n=int(input('Digite um numero: '))
print('fim')

s=0
for c in range(1,6):
    n=int(input('Digite o valor:'))
    s=n+s
print('A soma dos valores acima é {}'.format(s))