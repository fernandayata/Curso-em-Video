frase = str(input('Digite uma frase: ')).strip().upper() #elimina espaços antes e depois da frase
palavras = frase.split() #elimina espaços internos
junto = '' .join(palavras) #elimina espaços internos
inverso = ''
for letra in range(len(junto) -1, -1, -1):
  inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
  print('Temos um palídromo!')
else:
  print('A farse digitada não é um palídromo!')


