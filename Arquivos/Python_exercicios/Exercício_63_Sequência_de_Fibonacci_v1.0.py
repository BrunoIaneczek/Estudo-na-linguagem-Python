'''Escreva um programa que leia um numero n inteiro
qualquer e mostre na tela  os n primeiros elementos de uma
sequência de fibonacci
EX 0>1>1>2>3>5>8'''


termos = int(input('Quantos termos vc quer mostrar '))
t1 = 0
t2 = 1
t3 = t1+t2
c = 0
while c <= termos-1:
      t3 = t1 + t2
      c+=1
      print(t3)
      t1=t2
      t2=t3




