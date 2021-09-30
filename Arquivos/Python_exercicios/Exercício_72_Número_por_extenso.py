'''Crie um programa que tenha uma tupla totalmente
preenchida com uma contagem por
extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado
e mostra-lo por extenso'''

numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze',
           'treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    resp = ''
    num = int(input('Digite um número para lê-lo por extenso: '))

    while num < 0 or num > 20:
        num = int(input('Tente novamente.Digite um número para lê-lo por extenso: '))

    print(f'Você digitou o número {numeros[num]}.')
    resp = str(input('Você deseja continuar [S/N]? ')).strip().lower()[0]
    if resp not in 'sn':
        resp = str(input('Você deseja continuar [S/N]? ')).strip().lower()[0]
    if resp == 'n':
        break


