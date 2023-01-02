listagem = []
suporte = []
maior = menor = cont = 0
menu = ''

while menu != 'n':
  suporte.append(str(input('\nNome: ')))
  peso = int(input('Peso: '))
  suporte.append(peso)
  menu = str(input('Quer continuar? [S/N]: ')).lower()
  if cont == 0:
    maior = menor = peso
  elif peso >= maior:
    maior = peso
  elif peso <= menor:
    menor = peso
  listagem.append(suporte[:])    
  suporte.clear()
  cont += 1 
   
print(f'Ao todo foram cadastrados {cont} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for c in listagem:
  if c[1] == maior:
    print(f'{c[0]}...', end='')
print()    
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for c in listagem:
  if c[1] == menor:
    print(f'{c[0]}...', end='')
print()
