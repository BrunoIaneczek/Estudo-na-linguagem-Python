frase= '  curso em video python  '
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print(frase.count("o"))
print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))#conta total de caracteres incluindo os espaços
print(len(frase.strip())) #strip limpa todos os espaços antes e depois da string
frase2 = 'O assassino mora ao lado'
print(frase2.replace('mora', 'vive')) #replace troca uma string por outra( caso queira salvar a mudança utilize
#frase2 = frase2.replace('mora', 'vive')

print('curso' in frase) #verifica se existe na estring a palavra
print(frase2.find('O')) #verifica a posição(a string tem q ser exatamente igual a procurada, seguindo maiscula, minisculas e acentos
print(frase.split()) #cria uma lista apartir de uma string
lista = frase.split()
print(lista[0]) #escreve a string na lista seguindo posição solicitada
print(lista[0][1]) #mostra  a string e logo apos a letra da mesma solicitada
print('''texto entre 3 aspas 
para ler todo sem precisar
escrever print toda linha''')
