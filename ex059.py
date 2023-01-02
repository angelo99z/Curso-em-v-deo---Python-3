from time import sleep
print('\n---------- ### ----------\n')
print('Digite dois números: ')
n1 = int(input('n1: '))
n2 = int(input('n2: '))
print('\nEscolha uma opção: ')
print('''[ 1 ] SOMAR 
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA
  ''')
menu = int(input('Opção: '))

while menu != 0:
  if menu == 1:
    print('Opção selecionada: [ 1 ] SOMAR')
    soma = n1 + n2
    sleep(0.8)
    print('\nSoma: {}'.format(soma))
    sleep(1.5)
    print('\nEscolha uma opção: ')
    print('''[ 1 ] SOMAR 
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA
  ''')
    menu = int(input('Opção: '))
  elif menu == 2:
    print('Opção selecionada: [ 2 ] MULTIPLICAR')
    mult = n1 * n2
    sleep(0.8)
    print('\nMultiplicação: {}'.format(mult))
    sleep(1.5)
    print('\nEscolha uma opção: ')
    print('''[ 1 ] SOMAR 
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA
  ''')
    menu = int(input('Opção: '))
  elif menu == 3:
    print('Opção selecionada: [ 3 ] MAIOR')
    sleep(0.8)
    if n1 > n2:
      print('\nMaior: {}'.format(n1))
    elif n2 > n1:
      print('\nMaior: {}'.format(n2))
    sleep(1.5)
    print('\nEscolha uma opção: ')
    print('''[ 1 ] SOMAR 
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA
  ''')
    menu = int(input('Opção: '))  
  elif menu == 4:
    print('Opção selecionada: [ 4 ] NOVOS NÚMEROS')
    sleep(0.8)
    print('Digite dois números: ')
    n1 = int(input('n1: '))
    n2 = int(input('n2: '))
    print('\nEscolha uma opção: ')
    print('''[ 1 ] SOMAR 
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA
  ''')
    menu = int(input('Opção: ')) 
  elif menu == 5:
    quit()
  else:
    sleep(0.5)
    print('\n!!!Digite uma opção válida!!!\n')
    sleep(1.5)
    print('''[ 1 ] SOMAR 
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA
  ''')
    menu = int(input('Opção: '))