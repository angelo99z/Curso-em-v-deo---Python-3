from time import sleep
print('\n---------- ### ----------')
sexo = str(input('\nDigite o seu sexo [M/F]: ')).lower()
while sexo != 'm' and sexo != 'f':
  if sexo!= 'm' and sexo != 'f':
    print('\n!!!Digite um valor válido [M/F]!!!')
    sleep(1.5)
  print('\n---------- ### ----------')
  sexo = str(input('\nDigite o seu sexo [M/F]: ')).lower()  
print('\n---------- FIM ----------\n')