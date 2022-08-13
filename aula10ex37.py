num = int(input('Digite um número'))
print('''Escolha uma das bases para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
Option = int(input('Sua opção:')) 
if Option == 1:
  print('{} convertido para binário é igual a {}'.format (num, bin(num)))
elif Option == 2:
  print('{} convertido para octal é igual a {}'.format (num, oct(num)))
elif Option == 3:
  print('{} convertido para hexadecimal é igual a {}'.format (num, hex(num)))


