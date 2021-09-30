sec = int(input())
hora = sec//3600
minutos = (sec - hora*3600)//60
segundos = sec-(hora*3600 + minutos*60)
print(f'{hora}:{minutos}:{segundos}')
