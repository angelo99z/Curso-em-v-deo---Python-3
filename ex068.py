import random
from time import sleep

print('-=-'*15, '\n           JOGO DO PAR OU IMPAR\n', '-=-' *15)
c = 0
while True:
  n = int(input('Escolha um número: '))
  player = str(input('Par ou impar? [P / I]: ')).lower()
  cpu = ''
  cpun = random.randint(1, 10)
  print('A máquina escolheu...')
  sleep(1)
  print(cpun)
  sleep(0.5)
  if player == 'p' or player == 'i':
    if player == 'p':
      cpu = 'i'
    else:
      cpu = 'p'
    if (cpun + n) % 2 == 0:
      if player == 'p':
        print('Parabés!!! você venceu\n')
      else:
        print('Você perdeu\n')
        break
    if (cpun + n) % 2 == 1:
      if player == 'p':
        print('Você perdeu\n')
        break
      else:
        print('Parabéns!!! você venceu\n')   
  else:
    print('\n!!!Digite um valor válido !!!')
  c += 1  

print(f'Você venceu {c} vezes consecutivas')    
print('FIM\n')