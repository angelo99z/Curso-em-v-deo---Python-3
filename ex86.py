'''matriz = []
linha1 = []
linha2 = []
linha3 = []
cont = 0

for c in range(3):
  linha1.append(int(input(f'Digite um valor para [0, {c}]: ')))
for c in range(3):
  linha2.append(int(input(f'Digite um valor para [1, {c}]: ')))  
for c in range(3):
  linha3.append(int(input(f'Digite um valor para [2, {c}]: ')))
  
for c in range(3):
  print(f'[   {linha1[c]}   ]', end='')
print()  
for c in range(3):
  print(f'[   {linha2[c]}   ]', end='')
print()  
for c in range(3):
  print(f'[   {linha3[c]}   ]', end='') '''
  
matriz = [[0, 0, 0],[0, 0, 0], [0, 0, 0]] 
for l in range(3): # faz dois for um passando por cada linha e outro passando por cada coluna, após inserir os 3 dados da coluna de uma linha, pula para outra linha e repete o processo.
  for c in range(3): # segundo for, adicionando os dados na coluna
    matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}] : '))
    
print('-=' * 30)
for l in range(3):
  for c in range(3):
    print(f'[{matriz[l][c]:^5}]', end='') # :^5 formata o print para ser exibido de forma centralizado com 5 casas
  print()

