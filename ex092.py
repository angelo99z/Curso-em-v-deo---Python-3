trabalhador = {}
trabalhador['nome'] = str(input('\nNome: '))
trabalhador['idade'] = int(input('Ano de nascimento: '))
nasc = trabalhador['idade']
trabalhador['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
trabalhador['idade'] = 2022 - trabalhador['idade']

if trabalhador['ctps'] == 0:
  print('-='*30)
  print(f'nome tem o valor {trabalhador["nome"]}')
  print(f'Idade tem o valor {trabalhador["idade"]}')
  print(f'ctps tem o valor {trabalhador["ctps"]}')
  print('-='*30)
else:
  trabalhador['contratação'] = int(input('Ano de contratação: '))
  trabalhador['salário'] = int(input('Salário (R$): '))
  trabalhador['aposentadoria'] = (trabalhador['contratação'] - nasc) + 35
  print('-='*30)
  print(f'nome tem o valor {trabalhador["nome"]}')
  print(f'Idade tem o valor {trabalhador["idade"]}')
  print(f'ctps tem o valor {trabalhador["ctps"]}')
  print(f'contratação tem o valor {trabalhador["contratação"]}')
  print(f'salário tem o valor {trabalhador["salário"]}')
  print(f'aposentadoria tem o valor {trabalhador["aposentadoria"]}')
  print('-='*30)  
  