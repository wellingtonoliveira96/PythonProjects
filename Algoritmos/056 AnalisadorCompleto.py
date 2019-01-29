'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''

idadeT = 0
idadeM = 0
maisV = 0
maisN = 0
menorV = 0
nomeV = ''
for pessoa in range(1, 5, 1):
    print('-' * 20 + ' {}ª PESSOA '.format(pessoa) + '-' * 20)
    nome = str(input('Digite o seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [F/M]: '))
    idadeT += idade
    if sexo == 'F':
        if idade < 20:
            menorV += 1
    elif pessoa == 1 and sexo == 'M':
        maisV == idade
        maisN == idade
    else:
        if sexo == 'M':
            if idade > maisV:
                nomeV = nome
                maisV = idade
            if idade < maisN:
                maisN = idade
idadeM = idadeT / 4
print('O nome do homem mais velho é {}'.format(nomeV))
print('Existem {} mulheres com menos de 20 anos no grupo'.format(menorV))
print('A média de idade do grupo é {}'.format(idadeM))

