print ('='*40)
print('     10 TERMOS DE UMA PA     ')
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
pa = 0
pa = termo + (10 - 1) * razao
for count in range(termo, pa + razao, razao):
    print('{} '.format(count), end=' ->')

