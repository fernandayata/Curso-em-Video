peso = float(input('Digite seu peso (kg)'))
altura = float(input('Digite sua altura (m)'))
imc = peso / (altura ** 2)
print(' O ICM é {:.1f}'.format(imc))
if imc < 18.5:
  print('Você está abaixo do peso normal')
elif 18.5 <= imc < 25: #peso entre 18.5 e 25
  print('Parabéns! Você está na faixa de peso normal')
elif 25 <= imc < 30:
  print('Você está em sobrepeso!')
elif 30 <= imc < 40:
  print('Você está em obesidade! CUIDADO!') 
else:
  print('Você está em obesidade mórbida! CUIDADO!') 
  
