'''Supondo que a população de um país A seja da ordem de 80000 habitantes
com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma
taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários
para que a população do país A ultrapasse ou iguale a população do país B,
 mantidas as taxas de crescimento.'''

paisA = 80000
paisB = 200000
c = 0
while paisA <= paisB:
    paisB+=(paisB*1.5)/100
    paisA+=(paisA*3)/100
    c += 1
print(f'Após {c} anos população do pais A {paisA:.2f}   e   poulação do pais B {paisB:.2f}')

















