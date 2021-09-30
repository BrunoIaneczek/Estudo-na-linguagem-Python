#Faça um programa que leia algo pelo teclado e mostre seu tipo primitivo e todas as informações possiveis sobre ele.

algo = (input('digite algo:  '))
print(algo)
print('o tipo primitivo deste valor é', type(algo))
print('o valor é um numero?',algo.isnumeric())
print('o valor e alfabético? ',algo.isalpha())
print('o valor é decimal? ',algo.isdecimal())
print('o valor esta maisculo? ',algo.isupper())
print('o valor esta em minusculo? ',algo.islower())