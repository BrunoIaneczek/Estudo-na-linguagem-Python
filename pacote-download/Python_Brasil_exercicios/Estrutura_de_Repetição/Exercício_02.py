'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
 mostrando uma mensagem de erro e voltando a pedir as informações.
'''

while True:
    user = str(input('Digite se usuário: '))
    senha = str(input('Digite sua senha: '))
    while user == senha:
        print('Usuário e senha identicos!')
        user = str(input('Digite se usuário: '))
        senha = str(input('Digite sua senha: '))
    print('Acesso aceito!')
    break


