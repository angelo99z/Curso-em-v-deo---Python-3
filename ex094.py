dados = {}
todos = []
menu = ''
média = []

while menu != 'n':
  dados['nome'] = str(input('\nNome: '))
  dados['sexo'] = str(input('Sexo [M/F]: '))
  dados['idade'] = int(input('Idade: '))
  média.append(dados['idade'])
  todos.append(dados.copy())
  menu = str(input('Quer continuar? [S/N]: ')).lower()
  while menu != 'n' and menu != 's':
    print('ERRO!  Responda apenas S ou N.\n')
    menu = str(input('Quer continuar? [S/N]: ')).lower()
    
média = sum(média)/len(todos)    
print(f'\nA) Ao todos temos {len(todos)} pessoas cadastradas.')
print(f'B) A média de idade é de {média} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for c in todos:
  if c['sexo'] == 'f':
    print(c["nome"], end=' ')
print()    
print(f'D) Lista das pessoas que estão com a idade acima da média:')
for c in todos:
  if c['idade'] > média:
    print(f'    nome = {c["nome"]}; sexo = {c["sexo"]}; idade = {c["idade"]}')
    
print('<<  ENCERRADO  >>\n')
