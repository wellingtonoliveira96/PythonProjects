from random import randint
print('''Sou seu computador...
Acabei de pensar em um número entre 1 e 10. 
Será que você consegue adivinhar qual foi?
''')
tentativas = 0
pensei = randint(0, 10)
teste = 0

while teste == 0:
    palpite = int(input('Qual é o seu palpite?'))
    if palpite != pensei:
        print('Você errou. Tente novamente!')
        tentativas += 1
    elif palpite == pensei:
        print('''Você acertou. Eu pensei no número {}. 
        Você levou {} vezes para acertar.'''.format(pensei, tentativas)
              )
        teste = 1

