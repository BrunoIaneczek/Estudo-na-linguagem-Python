'''Crie um programa que tenha uma tupla única com nomes
produtos e seus respesctivos preços na sequẽncia.
No final, mostre uma listagem de preços organizando os dados
em forma tabular'''
print(20*'--')
print(f'{"LISTAGEM DE PREÇOS":^40}')
print(20*'--')
listagem = ('lápis',1.75,'borracha',2.00,'caderno',15.90,'estojo',25.00,'transferidor',
            4.20,'compasso',9.99,'mochila',120.32,'canetas',22.30,'livro',34.90)
for c in range(0,17,2):
    print(f'{listagem[c]:.<30}',end=''),print(f'R${listagem[c+1]:>4.2f}')

    ''' for c in range(0,len(palavras[0])):
        if (palavras[0][c]) in ('a','e','i','o','u'):
            print(palavras[0][c])'''