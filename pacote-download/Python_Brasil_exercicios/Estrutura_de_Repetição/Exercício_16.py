'''A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500.'''
fibonacci = []
anterior = 0
atual = 1
posterior = 1

while posterior != 999:
    posterior = atual + anterior
    anterior = atual
    atual = posterior
    fibonacci.append(posterior)
    if posterior > 500:
        break
print(fibonacci)