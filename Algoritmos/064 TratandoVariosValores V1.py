valor = 0
total = 0
cont = 0
while valor != 999:
    valor = int(input('Digite um número [999 para parar]: '))
    if valor != 999:
        total += valor
        cont += 1
print('Você digitou {} números e a soma entre eles foi de {}'.format(cont, total))