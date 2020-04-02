from random import randint
v = 0
while True:
    player = int(input('Diga um valor: '))
    computer = randint(0, 10)
    total = player + computer
    choice = ' '
    while choice not in 'PI':
        choice = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {player} e o computador jogou {computer}. Total de {total}', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if choice == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif choice == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER!Você venceu {v} vezes.')