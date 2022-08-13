casa = float(input('Digite o valor da casa'))
salario = float(input('Digite o valor do salario')) 
anos = int(input('Digite em quantos anos irá pagar'))
parcelas = casa / (anos*12)
minimo = salario * 30 / 100
print('Para pagar a casa que custa {:.2f} em {} anos, serão cobradas parcelas mensais de {:.2f} reais'.format(casa, anos,parcelas), end="")
if parcelas <= minimo:
  print('O impréstimo foi CONCEDIDO!')
else:
  print('O impréstimo foi NEGADO!')
