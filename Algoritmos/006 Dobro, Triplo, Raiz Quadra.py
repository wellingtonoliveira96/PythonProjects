num = float(input('Digite um valor:'))
dobro = num * 2
triplo = num * 3
raizq = num**0.5
raizc = num**0.3
print('O dobro de {} vale {} \n O triplo de {} vale {}'.format(num,dobro,num,triplo))
print('A raiz quadrada de {} vale {:.2f} \n A raiz cúbica de {} vale {:.2f}'.format(num,raizq,num,raizc))
#função pow também calcula a raiz. Exemplo: pow(num, (1/2)