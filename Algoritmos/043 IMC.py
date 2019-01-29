peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print('Com peso de {}kg e altura de {}m'.format(peso,altura))
if imc <= 18.5:
    print('Seu IMC está em {}. Você está abaixo do peso'.format(imc))
elif imc <= 25:
    print('Seu IMC está em {}. Você está no seu peso ideal'.format(imc))
elif imc <= 30:
    print('Seu IMC está em {}. Você está com Sobrepeso'.format(imc))
elif imc <= 40:
    print('Seu IMC está em {}. Você está com Obesidade'.format(imc))
else:
    print('Seu IMC está em {}. Você está com Obesidade Mórbida'.format(imc))