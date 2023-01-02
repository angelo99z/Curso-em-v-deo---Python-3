from time import sleep
jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input(f'Quandos partidas {jogador["nome"]} jogou? '))

for c in range(jogador['partidas']):
  gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
  
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('-=' *45)
print(jogador)
sleep(2)
print('-=' *45)
print(f'O campo nome tem o valor {jogador["nome"]}')
print(f'O campo gols tem o valor {jogador["gols"]}')
print(f'O campo total tem o valor {jogador["total"]}')
print('-=' *45)
sleep(2)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')

for k, g in enumerate(gols):
  print(f'    => Na partida {k}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
  