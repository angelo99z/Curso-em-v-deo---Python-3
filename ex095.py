from time import sleep
jogs = []
jog = {}
gols = []
cont = 0

while True:
  jog['nome'] = str(input('\nNome do Jogador: '))
  jog['partidas'] = int(input(f'Quantas partidas {jog["nome"]} jogou? '))
  print()
  for c in range(jog['partidas']):
    gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    
  jog['gols'] = gols[:]
  jog['total'] = sum(gols)
  jogs.append(jog.copy())
  gols.clear()
  menu = str(input('Quer continuar? [S/N] ')).upper()
  if menu != 'S':
    break 
print(jogs[0]['gols'][0])  

print('-='*45)
print('cod ', end='')
for i  in jog.keys():
  print(f'{i:<14}', end=' ')
print()        
print('--'*45)
for k, v in enumerate(jogs):
  print(f'{k:>3}', end=' ')
  for d in v.values():
    print(f'{str(d):<15}', end='')
  print()  
'''for c in jogs:
  print(f'{cont}    {c["nome"]:<18} {c["gols"]} {c["total"]:>10}')
  cont += 1'''
while True:
    menu = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    cont = 0
    if menu == 999:
      break
    elif menu <= len(jogs):
      print(f'-- LEVANTAMENTO DO JOGADOR {jogs[menu]["nome"]}:')
      sleep(1)
      for c in jogs[menu]:
        while cont < len(jogs[menu]['gols']):
          print(f'No jogo {cont+1} fez {jogs[menu]["gols"][cont]} gols.')
          cont += 1
    else:
        print('-='*30)
        print(f'ERRO! Não existe jogador com o código {menu}!')
        print('-='*30)
        