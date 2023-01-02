import random
from time import sleep
print('\n')
print('-=-'*10, 'JOKEMPO', '-=-'*10)
jokempo = ['pedra', 'papel', 'tesoura']
print('\nDigite PEDRA, PAPEL, ou TESOURA e tente ganhar da máquina: \n')
player = str(input())
player = player.lower()
maquina = random.choice(jokempo)
if player == 'pedra' or player == 'papel' or player == 'tesoura':
  print('\n'*30)
  print('\nJO\n')
  sleep(0.5)
  print('KEN\n')
  sleep(0.5)
  print('PO\n')
  sleep(0.5)
  print('\n'*30)
  print('A escolhada máquina foi...')
  sleep(1.5)
  print('\n'*3)
  print(maquina.upper())
  if maquina == 'pedra':
    if player == 'pedra':
      print('\nEMPATE')
      print('\n'*3)
    elif player == 'papel':
      print('\nVOCÊ GANHOU')
      print('\n'*3)
    else:
      print('\nA MÁQUINA GANHOU')
      print('\n'*3)
  elif maquina == 'papel':
    if player == 'pedra':
      print('\nVOCÊ PERDEU')
      print('\n'*3)
    elif player == 'papel':
      print('\nEMPATE')
      print('\n'*3)
    else:
      print('\nVOCÊ GANHOU')
      print('\n'*3)    
  elif maquina == 'tesoura':
    if player == 'pedra':
      print('\nVOCÊ GANHOU')
      print('\n'*3)
    elif player == 'papel':
      print('VOCÊ PERDEU')
      print('\n'*3)
    else:
      print('\nEMPATE')
      print('\n'*3)
else:
  print('\n!!!Digite um valor válido!!!')
  print('\n'*3)
  
  '''
  from random import randint
  itens = ('Pedra', 'Papel, 'Tesoura')
  computador = randint(0, 2)
  print("Suas opções:
  [ 0 ] PEDRA
  [ 1 ] PAPEL
  [ 2 ] TESOURA")
'''