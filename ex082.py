numeros = []
pares = []
impares = []
menu = ''
while menu != 'n':
  n = int(input('Digite um número: '))
  numeros.append(n)
  menu = str( input('Quer continuar? [S/N]: '))
  if n % 2== 0:
    pares.append(n)
  else:
    impares.append(n)
print('=-'*30)    
print(f'Todos os números digitados: {numeros}')
print(f'Números pares digitados: {pares}')
print(f'Números impares digitados: {impares}')
