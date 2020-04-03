idade = contM = contH = cont = 0
while True:
        print('-' * 30)
        print('CADASTRE UMA PESSOA')
        print('-' * 30)

        idade = int(input('Quantos anos você tem?'))

        sexo = ' '
        while sexo not in 'MF':
            sexo = str(input('Qual é o seu sexo? [M/F]')).strip().upper()[0]

        if idade >= 18:
            cont +=1

        if sexo == 'M':
            contH += 1

        if sexo == 'F' and idade < 20:
                contM += 1

        resp = ' '
        while resp not in 'SN':
            resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        if resp == 'N':
            break

print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas com mais de 18 anos: {cont}')
print(f'Ao todo temos {contH} homens cadastrados')
print(f'E temos {contM} mulheres com menos de 20 anos')

