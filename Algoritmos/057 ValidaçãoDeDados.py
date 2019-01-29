controle = 0
while controle == 0:
    sexo = str(input('Digite seu sexo: ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Dados inválidos. Por favor, informe seu sexo:')
    if sexo == 'M' or sexo == 'F':
        print('Sexo {} registrado com sucesso'.format(sexo))
        controle = 1
       #break

'''
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos.Por favor, informe seu sexo: ')).strip.upper()[0]
print('Sexo {} registrado com sucesso.format())
'''
