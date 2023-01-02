menu = ''
numeros = []

while menu != 'n':
  n = int(input('Digite um número: '))
  
  while n in numeros:
    print('!!!Valor duplicado!!!')
    n = int(input('Digite outro número: '))
    
  numeros.append(n)
  print('Valor adicionado com sucesso!')
  menu = str(input('Quer continuar? [S/N]: ')).lower()
  
print(f'Você digitou os valores {sorted(numeros)}')  
  