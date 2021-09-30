#módulos (crtl+espaço=lista de bibliotecas padrao)
#biblioteca matemática math

#import de todas as funçoes
import math
num = int(input('Digite um numero: '))
raiz =math.sqrt(num)
print('A raiz de {} é igaual a {}.'.format(num, math.floor(raiz)))

#import de funçao especifica e funções especificas
from math import sqrt
num =int(input('Digite um umero: '))
raiz =sqrt(num)
print('A raiz quadrada de {} é {}.'.format(num , raiz))
