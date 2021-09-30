'''Crie um site em python que verifique se o site pudim esta acessivel'''

import requests

try:
    site = requests.get('http://pudim.com.br/')
except:
    print('Não foi possivel aessar o site')
else:
    print('Site acessado com sucesso')
