from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
opcaoM = randint(0, 2)
print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
''')
opcaoJ = int(input('Qual é a sua jogada? '))

if opcaoJ > 2:
    print('OPÇÃO INVALIDA')
else:
    print('JO')
    sleep(0.3)
    print('KEN')
    sleep(0.3)
    print('PO!!!')
    sleep(0.3)

    print('-=-' * 20)
    print('COMPUTADOR jogou {}'.format(itens[opcaoM]))
    print('JOGADOR  jogou {}'.format(itens[opcaoJ]))
    print('-=-' * 20)


    if opcaoJ == 0 and opcaoM == 1: # papel embrulha pedra
        print('COMPUTADOR VENCE')
    elif opcaoJ == 2 and opcaoM == 0: #pedra amassa tesoura
        print('COMPUTADOR VENCE')
    elif opcaoJ == 1 and opcaoM == 2: #tesoura corta papel
        print('COMPUTADOR VENCE')
    elif opcaoJ == 1 and opcaoM == 0: #papel embrulha pedra
        print('JOGADOR VENCE')
    elif opcaoJ == 0 and opcaoM == 2: #pedra amassa tesoura
        print('JOGADOR VENCE')
    elif opcaoJ == 2 and opcaoM == 1: #tesoura corta papel
        print('JOGADOR VENCE')
    elif opcaoJ == opcaoM:
        print('EMPATE. TENTE NOVAMENTE!')
