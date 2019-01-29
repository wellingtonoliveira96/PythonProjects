from datetime import date
atual = date.today().year
ano = int(input('Digite seu ano de nascimento:  '))
idade = atual - ano
falta = 18 - idade
anoA = falta + atual
passou = idade - 18
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
if idade == 18:
    print('Você deve se Alistar, procure a junta militar de seu município')
if idade < 18:
    print('Ainda faltam {} anos para o seu alistamento'.format(falta))
    print('Seu alistamento será em {}'.format(anoA))
else:
    print('Você já deveria ter se alistado há {} anos'.format(passou))
