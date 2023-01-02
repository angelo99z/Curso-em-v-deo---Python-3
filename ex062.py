from time import sleep
print('-=-'*5, 'RAZÃO ARITMÉTICA', '-=-'*5)
pt = int(input('Digite o primeiro termo (inteiro): '))
r = int(input('Digite o valor da razão(inteiro): '))
print('Calculando...')
sleep(1)
c = 10
print(pt)
while c > 0:
  pt = pt + r
  c -= 1
  sleep(0.3)
  print(pt)

sleep(1.5)
print('\nDeseja adicionar MAIS termos ou SAIR ?\n')
print('''[ MAIS ]
[ SAIR ]''')
menu = str(input('\nSelecione uma opção: ')).lower()

if menu == 'mais':
  print('Opção selecionada [MAIS]')
  sleep(0.5)
  c = int(input('Quantos termos a mais deseja imprimir?  '))
  while c > 0:
    pt = pt + r
    c -= 1
    sleep(0.3)
    print(pt)
elif menu == 'sair':
  print('\nOpção selecionada [SAIR]')
  sleep(1)
  print('Saindo...')
  sleep(1)
  print('-=-'*5, 'FIM', '-=-'*5)
  quit()
else:
  print('\n!!!Digite uma opção válida!!!')      
print('-=-'*5, 'FIM', '-=-'*5)