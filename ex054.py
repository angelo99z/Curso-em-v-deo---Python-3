x = 0
z = 0
for c in range(1, 8):
  idade = int(input('Digite uma idade: '))
  if idade >= 21:
    x += 1
  elif idade < 21:
    z += 1  
print('\n{} Pessoas ainda não atingiram a maioridade e {} pessoas já atingiram \n'.format(z, x))    