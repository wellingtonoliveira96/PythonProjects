soma = 0
cont = 0
for impar in range(0, 500, 3):
    if (impar % 3 == 0) and (impar % 2 != 0):
        cont = cont + 1 # poderia ser cont += c
        soma = soma + impar # poderia ser soma += c
print('A soma dos {} números ìmpares e múltiplos de 3 o intervalo entre 1 e 500 é {}'.format(cont, soma))