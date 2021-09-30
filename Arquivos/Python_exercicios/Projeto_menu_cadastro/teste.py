

while True:
    cadastroNovaPessoanome('lista')
    cadastroNovaPessoaidade('lista')
    resp = str(input('Mais alguem'))
    if resp in 'n':
        break