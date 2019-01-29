'''from math import factorial
num = int(input('''
    #Digite um número para descobrir seu fatorial
'''))
fat = 0
cont = 1
while cont != 0:
        fat = factorial(num)
        cont = 0
print(fat)'''

num = int(input('Digite um número para calcular seu Fatorial: '))
ctrl = num
fat = 0

while num > 1:
    if fat == 0:
        fat = ctrl * (num-1)
    else:
        fat = fat*(num-1)
    num -= 1
    print('{} x '.format(num), end='')
#print('{} x '.format(num), end='' + '='.format(fat))
print('= {} '.format(fat))