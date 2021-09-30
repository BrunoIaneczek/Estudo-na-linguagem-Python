'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''

area_a_ser_pintada = float(input('Digite o valor em metros quadradaos da área a ser pintada: '))
cobertura_tinta_litro = 6
latag = 18
latam = 3.6
preçolg = 80
preçolm = 25
print(' ')
litros = area_a_ser_pintada/cobertura_tinta_litro
if litros < 18:
    print('Você usará menos que uma lata de 18l de tinta,sendo assim compre \033[36m{:.2f}\033[m latas de 3.6l.'.format(litros//latam))
    print('E pagará o valor de \033[34mR${:.2f}\033[m'.format((litros//latam)*preçolm))
    li = litros//latam
    lit = li*latam
    dif = litros-lit
    #print(litros,li,dif,lit)
else:
    print('Você deve comprar \033[32m{:.2f}\033[m latas de 18l.'.format(litros//latag))
    print('E pagará o valor de \033[31mR${:.2f}.\033[m.'.format((litros//latag)*preçolg))
    li = litros // latag
    lit = li * latag
    dif = litros - lit
    print('E tera que comprar \033[34m{}\033[m lata/s de 3.6'.format(dif//latam))
    #print(litros, li, dif, lit)
    #print(litros)