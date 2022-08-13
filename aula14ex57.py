sexo =  str(input('Digite seu sexo [M,F]')).strip().upper()[0] #remover espaços; tornar a primeira letra maiúscula
while sexo not in 'MmFf':
   sexo = str(input('Inválido! Por favor informe seu sexo [M ou F]')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

