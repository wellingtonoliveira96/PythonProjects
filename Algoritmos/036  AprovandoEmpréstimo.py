casa = float(input('Digite o valor da casa a ser comprada: R$ '))
salario = float(input('Qual é o seu salário? R$'))
tempo = int(input('Em quantos anos pretende pagar? R$'))
parcela = casa / (tempo * 12)
minimo = salario * 0.3
print('Para pagar uma casa no valor de R${:.2f} em {} anos em parcelas de R${:.2f} você terá: '.format(casa,tempo,parcela))
if parcela <= minimo:
    print('Empréstimo Aprovado!')
else:
    print('Empréstimo Negado')
