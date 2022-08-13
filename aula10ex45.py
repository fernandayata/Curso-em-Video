from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint (0,2)
print(''' Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*10)
print ('O computador jogou {}'.format(itens[computador]))
print ('O jogador jogou {}'.format(itens[jogador]))
print('-='*10)
if computador == 0: #computador jogou pedra
  if jogador == 0:
    print('Empate')
  elif jogador == 1:
    print('O Jogador ganhou')
  elif jogador == 2:
    print('O computador ganhou')
  else:
    print('Jogada inválida')
elif computador == 1: #computador jogou papel
  if jogador == 0:
    print('o computador ganhou')
  elif jogador == 1:
    print('Empate')
  elif jogador == 2:
    print('O jogador ganhou')
  else:
    print('Jogada inválida')
elif computador == 2: #computador jogou tesoura
  if jogador == 0:
    print('O jogador ganhou')
  elif jogador == 1:
    print('O computador ganhou')
  elif jogador == 2:
    print('Empate')
  else:
    print('Jogada inválida')
   