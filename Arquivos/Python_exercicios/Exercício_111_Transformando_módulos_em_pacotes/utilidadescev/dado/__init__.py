import string


def leiadinheiro(msg):
        variavel = input(msg).strip()

        while variavel[0] not in '0,1,2,3,4,5,6,7,8,9':
                print(f'\033[31mERRO: "{variavel}" não é um valor válido\033[m ')
                variavel = input(msg)

        for digito in range(len(variavel)):
                if variavel[digito] in ',':
                         return float(variavel.replace(',', '.'))
        else:
                return float(variavel)



