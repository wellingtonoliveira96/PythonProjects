preco = menorPreco = total = contM = cont  = 0
nomeMenor = ' '
while True:
        nome = str(input('Qual é o nome do produto?'))
        preco = float(input('Qual é o preço do produto?'))
        cont += 1
        total += preco

        if preco >= 1000:
            contM += 1
        if cont == 1:
            menorPreco = preco
            nomeMenor = nome
        else:
            if preco < menorPreco:
                menorPreco = preco
                nomeMenor = nome

        compra = ' '
        while compra not in 'SN':
            compra = str(input('Finalizar Compra? [S / N]')).strip().upper()[0]
        if compra == 'S':
            break

print (total, contM, menorPreco, nomeMenor)