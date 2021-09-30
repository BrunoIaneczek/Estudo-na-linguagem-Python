# Faça um programaque leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# se ele ainda vai se alistar
# se é hora de se alistar
# se ja passou do tempo de alistamento
# seu programa também deverá mostrar o tempo que faltou ou que passou do prazo.

from datetime import  date
adn = int(input('Digite o ano em que nasceu: '))
at = date.today().year
idade = at-adn
if idade<18:
    print('Você irá se alistar daqui a \033[31m{}\033[m anos e seu ano de alisamento será \033[32m{}\033[m.'.format(18-idade,at+(18-idade)))
elif idade==18:
    print('Neste ano você irá ter q se alistar.')
else:
    print('Você deveria ter se alistado há \033[33m{}\033[m anos e seu ano de alistamento foi \033[33m{}\033[m.'.format(idade-18, at-(idade-18)))
