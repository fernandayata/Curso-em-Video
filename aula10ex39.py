from datetime import date
atual = date.today().year
nasc = int(input('Digite seu ano de nascimento'))
idade = atual - nasc
falta = 18 - idade
sobra = idade - 18
print('Quem nasceu em {} tem {} anos no ano atual'.format(nasc,idade))
if idade == 18:
  print('É hora de se alistar!')
elif idade > 18:
  print('Você já deveria ter se alistado há {} anos!'.format(sobra))
elif idade < 18:
  print('Você ainda não tem 18 anos! Faltam ainda {} anos para o alistamento!'.format(falta))
  
