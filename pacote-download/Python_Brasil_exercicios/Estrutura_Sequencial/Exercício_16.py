'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
 Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
'Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''

print(20 * '==', '\033[36mSistema loja de tintas\033[m', 20 * '==')
print(' ')
print(10 * '==', '\033[33mInformaçoes nescessárias\033[m', 10 * '==')
c = ' '
while c not in 'S':
    area = float(input('Por favor informe o valor em m² da area a ser pintada: '))
    cobertura = float(input('Por favor informe a capacidade de cobertura em m², da tinta por litro: '))
    valor = float(input('Por favor informe o valor da tinta: '))
    quantidade_lata = float(input('Quantos litros contem a lata a ser vendida: '))
    numero_litros = area / cobertura
    numero_latas = numero_litros / quantidade_lata
    preço_total = numero_latas * valor
    print(' ')
    print('O cliente deverá comprar \033[36m{:.1f}\033[m latas de tinta e pagará o valor \033[34mRS{:.2f}\033[m.'.format(numero_latas, preço_total))
    print(' ')
    c = str(input('Se deseja finalizar programa digite [sim] se deseja resetar informaçoes digite [resetar]: ')).strip().upper()[
        0]
    if c not in 'SR':
        print('Digite opção valida')
print('obrigado volte sempre!')

