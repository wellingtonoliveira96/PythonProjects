r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
    if r1 == r2 and r1 == 3 and r2 == r3:
        print('Este triângulo é EQUILÁTERO')
    elif (r1 == r2) or (r2 == r3) or (r3 == r1):
        print('Este triângulo é Isósceles')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Este triângulo é Escaleno')

else:
    print('Os segmentos cima NÃO PODEM FORMAR triângulo!')
