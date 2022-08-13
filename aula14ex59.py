primeirovalor = int(input('Digite o primeiro valor'))
segundovalor = int(input('Digite o segundo valor'))
option = 0
while option != 5:
  print('''Escolha uma opção?
  [1] somar   
  [2] multiplicar
  [3] maior   
  [4] novos num 
  [5] sair do programa'''
)
  option = int(input('Qual é a sua opção?'))
  if option == 1:
    resultado = primeirovalor + segundovalor
    print('O resultado de {} + {} é: {} '.format(primeirovalor,segundovalor,resultado))
  elif option == 2:
    resultado = primeirovalor * segundovalor
    print('O resultado de {} x {} é: {} '.format(primeirovalor,segundovalor, resultado))
  elif option == 3:
    if primeirovalor > segundovalor: 
      print('Entre {} e {}, o maior número é {}'.format(primeirovalor,segundovalor,primeirovalor))
    elif primeirovalor == segundovalor:
        print('Os valores {} e {} são iguais'.format(primeirovalor,segundovalor))
    else:
      print('O {} é maior que o {}'.format(segundovalor,primeirovalor))
  elif option == 4:
    print('Informe os números novamente')
    primeirovalor = int(input('Primeiro valor'))
    segundovalor = int(input('Segundo valor'))
  elif option == 5:
    print('finalizando o programa')
  else:
    print('Declaração inválida! Tente novamente')
  print('=-=' * 10)
print('Fim do programa! Volte sempre!')
