primeiro = int(input('Primeiro termo: '))
razao = int(input('razao'))
decimo = primeiro + (10-1) * razao
for c in range (primeiro, decimo, razao):
  print('{}'.format(c), end=' ')
print('ACABOU')
