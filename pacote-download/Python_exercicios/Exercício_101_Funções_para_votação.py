def voto(anodenascimento):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - anodenascimento
    if 16 <= idade < 18 or idade >= 65:
        return f'Sua idade é de {idade} e seu voto é opcional'
    elif idade < 16:
        return f'Sua idade é de {idade}  e você não vota'
    elif 65 > idade >= 18:
        return f'Sua idade é de {idade} e seu voto é obrigatorio'

while True:
    anodenascimento = int(input('Digite o ano de seu nascimeto (Digite zero para encerrar o programa): '))
    print(voto(anodenascimento))
    print(20 * '-=-')
    if anodenascimento == 0:
        print('fim do programa')
        break

