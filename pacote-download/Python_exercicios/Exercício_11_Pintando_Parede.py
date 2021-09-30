# Faça um programa que leia a largura e a altura  de uma parede em metros, calcule sua área e a quantidade de tinta nescessária
#para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

larg = float(input('Largura da parede: '))
alt = float(input('altura da parede: '))

print('sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt ,alt*larg))
print('para pintar sua parede, você precisará de {:.2f}l de tinta.'.format((larg*alt)/2))
