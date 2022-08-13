primeira = float(input('Digite a primeira nota'))
segunda = float(input('Digite a segunda nota'))
media = (primeira + segunda) /2
print('Tirando {} e {}, a media do aluno é de {}'.format(primeira, segunda, media))
if media >=7:
  print('APROVADO')
elif media < 5:
  print('REPROVADO')
elif media >= 5 and media <=6.9:
  print('RECUPERAÇÃO')

