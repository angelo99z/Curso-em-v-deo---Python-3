import random
from time import sleep

jogos = []
jogo = []
valor = 0
menu = ''
j = int(input('\nQuantos jogos você quer que eu sorteie? '))

print('==========================JOGO DA MEGASENA ==========================')
sleep(1)
for c in range(j):
  if c == 0:
    print(f'-=-=-=-=-=-=-=Sorteando {j} jogos-=-=-=-=-=-=-=')
    sleep(1)
  for cont in range(6):
    valor = random.randint(0, 60)
    if valor in jogo:
      valor = random.randint(0, 60)
    else:
      jogo.append(valor)
       
  sleep(0.7)  
  jogos.append(sorted(jogo))
  print(f'Jogo {c+1}: {jogos[c]}') 
  jogo.clear()
  
print('-=-=-=-=-=-=-=BOA SORTE-=-=-=-=-=-=-=\n')  
   