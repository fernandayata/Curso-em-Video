num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:#se for divisível:
      print('\033[33m')#pinta de amarelo
      tot +=1
    else:
        print('\033[31m') #pinta de vermelho
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso que ele É PRIMO')
else:    
    print('E por isso ele NÃO É PRIMO')
