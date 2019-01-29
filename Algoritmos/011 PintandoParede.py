altura = float(input('Digite a altura da parede que irá pintar: '))
largura = float(input('Digite a largura da parede que irá pintar: '))
area = altura * largura
tinta = area / 2
print('Sabendo que cada 1l de tinta rende 2 metros de parede. \n ')
print('A sua parede tem {}m de altura por {}m de largura tem {}m² de área '.format(largura,altura,area))
print('E precisa de {} litros de tinta' .format(tinta))