# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#A: Para homens: (72.7*h) - 58
#B: Para mulheres: (62.1*h) - 44.7

print(30*'==','\033[36mPROGRAMA QUE CALCULA SEU PESO IDEAL CONFORME SEU SEXO\033[m',30*'==')
sexo = str(input('Por favor digite qual e seu sexo [M/F]: ')).strip().lower()[0]
alt = float(input('Por favor digite sua altura: '))
if sexo == 'f':
    pif = (62.1 * alt) - 44.7
    print('Seu peso ideal, você sendo do sexo feminino, é de \033[31m{:.2f}.\033[m'.format(pif))
elif sexo == 'm':
    pim = (72.7*alt) - 58
    print('Seu peso ideal você sendo do sexo masculino é de \033[34m{:.2f}.\033[m'.format(pim))
else:
    print('sexo inválido')
