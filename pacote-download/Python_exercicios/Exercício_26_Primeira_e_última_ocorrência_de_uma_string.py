# faça um programa que leia  uma frase e mostre:
# quantas vezes aparece a letra 'a'
# Em que posiçao ela aparece a primeira vez
# Em que posição ele aparece a ultima vez

frase = str(input('Digite uma frase: ')).strip() #nao funciona com acentos a ultima e primeira letra, so a contagem
f = frase.upper()
a = f.count('A')
ã = f.count('Ã')
â = f.count('Â')
á = f.count('Á')
à = f.count('À')
print('A letra a parece {} vezes na frase'.format(a+ã+â+á+à))
(len(f))
print('A letra a apareceu a primeira vez na posição {}'.format(f.find('A')+1))
print('A letra a apareceu a ultima vez na posição {}'.format(f.rfind('A')+1))