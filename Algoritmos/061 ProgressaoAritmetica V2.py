print('Gerador de PA')
print('-=-' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 0
termo = primeiro
while cont <= 10:
    print('{} ->'.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
