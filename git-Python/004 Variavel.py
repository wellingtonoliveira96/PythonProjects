# O algoritmo recebe um dado e retorna informações sobre ele

x = input('Digite algo:')
print('O tipo primitivo deste valor é:', type(x))
print('Só tem espaços?', x.isspace())
print('É um número?', x.isnumeric())
print('É alfabético?', x.isalpha())
print('É alfanúmerico?', x.isalnum())
print('Está em maiúsculas?', x.isupper())
print('Está em minúsculas?', x.islower())
