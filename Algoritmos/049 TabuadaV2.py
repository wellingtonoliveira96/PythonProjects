num = int(input('Digite um número para ver sua tabuada: '))
for count in range (0, 11, 1):
    print('| {} x {:2} = {} |'.format(num, count, num * count))


