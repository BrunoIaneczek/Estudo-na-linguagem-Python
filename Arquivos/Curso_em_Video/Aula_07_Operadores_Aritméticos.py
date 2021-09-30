#ordem de precedência
#1- ()
#2- **                                 #pra quebrar a linha usa se  /n
#3- *, /, //, %                        #pra nao quebrar usase       end=' '
#4- +,-

n1 = int(input('digite valor1: '))
n2 = int(input('digite  valor2: '))
a = n1+n2
s = n1-n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('a soma entre os valores é {},a subtração é {},a divisão é {} e a multiplicação e {}'.format(a,s,d,m))
print('a potencia  é {} e a divisão inteira é {} '.format(e,di))

