'''Faça um programa que tanha uma função chamada
escreva(), que receba um texto qualquer como parâmetro
e mostre uma ensagem com o tamnho adaptável'''

def escreva(txt):
    tamanho = len(txt)+4
    print(tamanho*'=')
    print(f'  {txt}')
    print(tamanho*'=')


escreva('olA')
escreva('Meu nome e Bruno')
escreva('Toma esta chinelão ordinário calhorda!')