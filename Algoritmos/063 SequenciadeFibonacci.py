print('-' * 20)
print('Sequência de Fibonacci')
print('-' * 20)
cont = int(input('Quantos termos você quer mostrar? '))
atual = 1
anterior = 0
print('~' * 30)
print('{} -> {}'.format(anterior, atual), end='')
while cont != 2:
    proximo = anterior + atual
    print(' -> {}'.format(proximo), end='')
    anterior = atual
    atual = proximo
    cont -= 1
print(' -> FIM')
print('~'*30)