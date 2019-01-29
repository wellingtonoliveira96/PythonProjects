preco = float(input('Digite o valor do produto desejado: R$ '))
desc = preco - (preco * 0.05)
print('O produto desejado custa {:.2f} reais , mas com desconto sai por {:.2f} reais'.format(preco,desc))