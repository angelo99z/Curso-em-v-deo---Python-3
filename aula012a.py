nome = input(str('\nQual é o seu nome?: '))
if nome == 'Angelo':
  print('\nque nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
  print('\nseu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
  print('\nBelo nome feminino')
else:
  print('\nseu nome é bem normal')
print('\nTenha um bom dia {}\n'.format(nome))
