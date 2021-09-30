# A confederação nacional de natação precisa de um  programa que leia o ano de nascimento do atleta
# e mostre sua categoria, de acordo com a idade.
# até 9 anos : mirim
# até 14 anos: infantil
# até 19 anos: junior
# até 20 anos: sênior
# acima de 20 anos: master

from datetime import date
adn = int(input('Digite o ano de nascimento do atleta: '))
at = date.today().year
idade = at-adn
if idade<=9:
    print('O atleta tem \033[34m{}\033[m e sua categoria é mirim.'.format(idade))
elif 9 < idade <= 14:
    print('O atleta tem \033[34m{}\033[m e sua categoria é infântil.'.format(idade))
elif 14<idade<=19:
    print('A idade do atleta é \033[34m{}\033[m e sua categoria é junior.'.format(idade))
elif 19<idade<=20:
    print('A idade do atleta é \033[34m{}\033[m e sua categoria é sênior.'.format(idade))
else:
    print('A sua idade é de \033[34m{}\033[m e sua categoria é master.'.format(idade))
