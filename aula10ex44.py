print('{:^40}'.format('LOJAS GUANABARA'))
preco = float(input('preço das compras'))
print('''Formas de pagamento:
[1] à vista, dinheiro ou cheque
[2] à vista, cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''')
option = int(input('Qual é a opção?'))
if option == 1:
  total = preco - (preco *10/100)
elif option == 2:
  total = preco - (preco *5/100)
elif option == 3:
  total = preco
  parcela = total/2
  print('Sua compra será parcelada em 2x vezes de {:.2f}'.format(parcela))
elif option == 4:
  total = preco + (preco*10/100)
  totalparcelas = int(input('Quantas parcelas?'))
  parcela = total/totalparcelas
  print('Sua compra será parcelada em {} x de {:.2f} reais'.format(totalparcelas,parcela))
else:
  total = 0
  print('Opção inválida de pagamento! Tente Novamente')
print('Sua compra de {:.2f} reais, vai custar {:.2f} reais no final'.format(preco,total))



