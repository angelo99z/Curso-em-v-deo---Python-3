def jogador(nome='desconhecido', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if len(n) == 0:
    n = '<desconhecido>'
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    jogador(nome = n)
else:
    jogador(n, g)
