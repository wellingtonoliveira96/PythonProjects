from datetime import date
aatual = date.today().year
maior = 0
menor = 0
for count in range(1, 8):
    anoN = int(input('Em que ano a {}ª pessoa nasceu?'.format(count)))
    idade = aatual - anoN
    if idade > 18:
        maior += 1
    else:
        menor += 1
print('Há {} pessoas maiores de idade. Há {} pessoas menores de idade'.format(maior, menor))