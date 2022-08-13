from datetime import date
atual = date.today().year
ano = int(input('Digite o ano de nascimento'))
idade = atual - ano
print('O atleta nasceu em {} e tem {} anos'.format(ano,idade))
print('Classificação:')
if idade <= 7:
  print('MIRIM')
elif idade <= 14:
  print('INFANTIL')
elif idade <=19:
  print('JUNIOR')
elif idade <= 25:
  print('SENIOR')
else:
  print('MASTER')
  


