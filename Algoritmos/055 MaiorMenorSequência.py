menorP = 0
maiorP = 0
for count in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(count)))
    if count == 1:
        maiorP = peso
        menorP = peso
    else:
        if peso > maiorP:
            maiorP = peso
        if peso < menorP:
            menorP = peso
print('O maior peso lido foi de {}kg'.format(maiorP))
print('O menor peso lido foi de {}kg'.format(menorP))
