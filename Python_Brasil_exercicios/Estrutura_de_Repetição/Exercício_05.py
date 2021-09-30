""" Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.

 Valide a entrada e permita repetir a operação. """
c = 0
while True:
    paisA = float(input('Informe a população do pais A: '))
    paisB = float(input('Informe a população do pais B: '))
    taxaA = float(input('Informe taxa de crescimento do pais A: '))
    taxaB = float(input('Informe taxa de crescimento do pais B: '))
    while paisA < paisB:
        paisA += (paisA*taxaA)/100
        paisB += (paisB*taxaB)/100
        c += 1
    print(f'Em {c} anos a população do pais A será de {paisA:.2f} superando ou igualando a população do pais B '
              f'que será de {paisB:.2f}')
    resp = str(input('Deseja continuar?[S/N] '))
    while resp not in 'SsNn':
        resp = str(input('Responda sim ou não: '))
    if resp in 'Nn':
        print('Fim do programa')
        break
