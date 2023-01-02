menu = ''
numeros = []
cont = 0
for c in range(5):
  while menu != 'n':
    n = int(input('Digite um número: '))
    numeros.append(n)
    menu = str(input('Quer continuar? [S/N]:'))

print('--'*20) 
print(f'Foram digitados {len(numeros)} valores')
numeros.sort(reverse=True)
print(f'Lista decrescente: {numeros}')

if 5 in numeros:
  print('O número 5 está na lista')
else:
  print('O número 5 não está na lista')  
print('--'*20)   