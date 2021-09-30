#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura)-58

print(30*'==','\033[36mPROGRAMA QUE CALCULA SEU PESO IDEAL\033[m',30*'==')

alt = float(input('Digite sua altura: '))
pi = (72.7*alt)-58
print('Seu peso ideal é de \033[32m{:.2f}.\033[m'.format(pi))


