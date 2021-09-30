'''Crie uma tupla preenchida com os 20 primeiros colocados
da tabela do brasileirão.Na ordem de colocação.Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em oredem alfabética.
D) Em que posição na tabela esta o time do Fortaleza'''

times = ('São Paulo','Atlético-mg','Flamengo','Palmeiras','Internacional','Grêmio','Fluminense','Santos','Corinthians'
         ,'Ceara Sc','Bragantino','Aletico-Go','Fortaleza','Atlettico-Pr','Sport Recife','Bahia','Vasco da Gama'
         ,'Coritiba','Goias','Botafogo')

print(f'Os primeiros 5 colocados são {times[0]},{times[1]},{times[2]},{times[3]},{times[4]}.')
# ou deste modo
print(f'Os primeiros 5 colocados são {times[0:5]}')
print(30*'-=-')
print(f'Os 4 últimos colocados são {times[16]},{times[17]},{times[18]} e {times[19]}.')
# ou deste modo
print(f'As quatro ultimos colocados são {times[-4:]}')
print(30*'-=-')
print(sorted(times))
print(30*'-=-')

print(f'O time Fortaleza é o {times.index("Fortaleza")+1}º colocado.')