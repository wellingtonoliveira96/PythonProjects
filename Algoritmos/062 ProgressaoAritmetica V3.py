print('Gerador de PA')
print('-=-' * 20)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
cont = 0
termo = primeiro
ctrl = 0
aumento = 10
while aumento != 0:
    ctrl = ctrl + aumento
    while cont <= ctrl:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    aumento = int(input('Quantos termos você quer mostrar a mais'))
print('Progressão Finalizada com {} termos mostrados'.format(ctrl))
print('FIM')