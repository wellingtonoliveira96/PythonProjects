par = 0
for count in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(count)))
    if num % 2 == 0:
        par = par + num
        print(num)
    else:
        num = 0
        print('O número {} foi desconsiderado por ser ímpar!'.format(par))
print('A soma dos valores pares digitados foi {}'.format(par))
