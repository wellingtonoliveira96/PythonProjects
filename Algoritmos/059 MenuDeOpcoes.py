num1 = float(input('Primeiro valor: '))
num2 = float(input('Segundo valor: '))
total = 0
opcao = 0
escolha = 0
while opcao != 5:
    print('''
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior 
        [ 4 ] novos números
        [ 5 ] sair do programa
    ''')
    escolha = int(input('Qual é a sua opcção? '))
    if escolha == 1:
        total = num1 + num2
        print('A soma de {} e {} resulta {}'.format(num1,num2,total))
    elif escolha == 2:
        total = num1 * num2
        print('A multiplicação de {} e {} resulta {}'.format(num1,num2,total))
    elif escolha == 3:
        if num1 > num2:
            print('Entre {} e {} o maior valor é {}'.format(num1,num2,num1))
        else:
            print('Entre {} e {} o maior valor é {}'.format(num1,num2,num2))
    elif escolha == 4:
        num1 = float(input('Primeiro valor: '))
        num2 = float(input('Segundo valor: '))
    elif escolha == 5:
        print('Finalizando..')
        #break
        opcao = 5
    else:
        print('Opção Invalida! Tente Novamente')
    print('=-='*20)
print('Fim do Programa. Volte Sempre')