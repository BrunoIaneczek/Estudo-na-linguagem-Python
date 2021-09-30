# Crie um programa que leia o nome completo de uma pessoa e diga qual seu primeiro e ultimo nome.

nome = str(input('Digite seu nome completo ')).strip()
n = nome.split()
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu ultimo nome é {}'.format(n[len(n)-1]))
# maneira q usei
nt = n[::-1]
print('Seu ultimo nome é {}'.format(nt[0]))# maneira q usei