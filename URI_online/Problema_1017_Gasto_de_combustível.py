TempodeViagem = int(input())
Velocidade = int(input())
GastoMediodeCombustivel = 12
DistanciaPercorrida = TempodeViagem*Velocidade
LitrosnecessáriosparaViajem = DistanciaPercorrida / GastoMediodeCombustivel

print(f'{LitrosnecessáriosparaViajem:.3f}')