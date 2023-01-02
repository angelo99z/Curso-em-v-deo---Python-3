times = ('Atletico MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'America MG', 'Atletico GO', 'Santos', 'Ceará SC','Internacional', 'São Paulo', 'Athletico PR', 'Cuiaba', 'Juventude', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoence')

print(f'\n5 Primeiros colocados: {times[0:5]}')
print(f'\n4 Ultimos colocados: {times[16:20]}') # ou times[-4:]
print(f'\nTabela em ordem alfabética: {sorted(times)}')
print('\nPosição do time Chapecoence: {}° posição\n'.format(times.index('Chapecoence')+1))