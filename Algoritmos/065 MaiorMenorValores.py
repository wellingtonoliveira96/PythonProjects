num = 0
maior = 0
menor = 0
media = 0
total = 0
cont = 0
resposta = 's'
while resposta == 's':
    num = int(input('Digite um número: '))
    total += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < maior:
            menor = num
    resposta = str(input('Quer continuar? [S/N]'))
media = total / cont
print('Você digitou {} números e a média foi {}'.format(cont, media))
print('O maior valor foi de {} e o menor foi de {}'.format(maior, menor))