np = 0
cont = 0
num = int(input('Digite um número: '))
for count in range(1, num + 1):
    if num % count == 0:
        np = num
        print('\033[33m', end='')
        cont = cont + 1
    else:
        print('\033[31m', end='')
    print ('{} '.format(count), end='')
print('\n\033[m O número {} foi dívisivel {} vezes. '.format(num,cont))
if cont == 2:
    print('Por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
