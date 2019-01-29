print('{:=^40}'.format('SKYWALKER STORE'))
preco = float(input('Digite o valor de sua compra: '))
print('''Escolha a Forma de Pagamento:
[ 1 ] À VISTA DINHEIRO/CHEQUE
[ 2 ] À VISTA NO CARTÃO
[ 3 ] 2 PARCELAS NO CARTÃO
[ 4 ] 3 OU MAIS PARCELAs NO CARTÃO
''')
opcao = int(input('Digite o número da forma escolhida: '))
if opcao == 1:
    valorF = preco - (preco * 0.10)
    print('A sua compra de RS{:.2f} sairá por {:.2f} com 10% de desconto ao escolher esta formada de pagamento'.format(preco,valorF))
elif opcao == 2:
    valorF = preco - (preco * 0.05)
    print('A sua compra de R${:.2f} sairá por R${:.2f} com 5% de desconto ao escolher esta forma de pagamento'.format(preco,valorF))
elif opcao == 3:
    valorF = preco
    print('A sua compra de R${:.2f} sairá pelo mesmo valor ao escolher esta forma de pagamento'.format(preco))
elif opcao == 4:
    numP = int(input('Forneça o número de parcelas: '))
    valorF = preco + (preco * 0.20)
    valorP = valorF / numP
    print('A sua compra de R${:.2f} sairá por R${:.2f} com 20% de juros em parcelas iguais de R${:.2f}'.format(preco, valorF, valorP))
else:
    print('Opção Invalida, tente novamente!')


