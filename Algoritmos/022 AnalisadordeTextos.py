'''

frase = 'Curso em Vídeo Python'

print(frase[3:])
print(frase[3:13])
print(frase[:13])
print(frase[1:15:2])
print(frase[::2])

print(""" fazendo isso podemos colocar textos grandes dentro de um mesmo print hehe. Python é muito foda
""") #fazendo isso = usando três aspas duplas

print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))

print(frase.replace('Python', 'Android')) #não muda de maneira permanente
print(frase)
frase = frase.replace('Python', 'Android')
print(frase)

print('Curso' in frase)
print(frase.find('deo'))
print(frase.find('video'))
print(frase.lower().find('vídeo'))

print(frase.split())

dividido = frase.split()
print(dividido[0])
print(dividido[2][3])

'''

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maíusculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])) )
