a , b = input().split(' ')
a = int(a)
b = int(b)

am = [0,1,2,3,4,5,6,7,8,9,10,11,12]
pm = [13,14,15,16,17,18,19,20,21,22,23]
if b in am and a in pm:
    tempo = 24 - a + b
elif a==b:
    tempo = 24
elif a in am and b in pm:
    tempo = b - a
elif a in pm and b in pm:
    if a>b:
        tempo = a-b
    else:
        tempo = b - a
elif a in am and b in am:
    if a>b:
        tempo = 24-a + b
    else:
        tempo = b - a
print(f'O JOGO DUROU {tempo} HORA(S)')