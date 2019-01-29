# O usúario digita um valor e o programa retorna o antecessor e o sucessor do valor

#Com as operações acontecendo dentro de variáveis

valor = int(input('Digite um número\n'))
ant = valor - 1
suc = valor + 1
print('Analisando o valor {}, seu antecessor é {} e seu sucessor é {}'.format(valor, ant, suc))



#Com as operações acontecendo no input, dentro do método format
num = int(input('Digite um valor:\n'))
print('Analisando o valor {}, seu antecessor é {} e o seu sucessor é {}'.format(num,(num-1), (num+1)))

