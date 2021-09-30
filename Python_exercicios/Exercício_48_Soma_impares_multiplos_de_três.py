# Faça um programa que calcule a soma entre todos os numeros impares
# que são multiplos de 3 e que se encontram entre 1 e 500

soma = 0 #acumulador
cont = 0 #contador
for c in range(1, 500):
    if c % 3==0 and not c % 2==0:
        soma += c
        cont +=1
print('A soma de todos os {} estes numeros é {}.'.format(cont,soma))



