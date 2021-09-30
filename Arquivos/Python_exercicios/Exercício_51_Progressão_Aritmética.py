#Desenvolva um programa que leia o primeiro termo de uma PA e sua razão.
# No final, mostre os 10 primeiros termos dessa PA.
t1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
tt = t1 + (10-1)*r
print(tt)
for c in range(t1,tt+r,r):
    print(c,end='>')

print('São os 10 primeiros termos da PA')



