numeros = []
pares = []
impares = []
print()
for c in range(7):
  n = int(input(f'Digite o {c+1}° número: '))
  if n % 2 == 0:
    pares.append(n)
  else:
    impares.append(n)
    
numeros.append(pares)
numeros.append(impares)
print(f'\nOs valores pares digitados foram: {sorted(pares)}')
print(f'Os valores impares digitados foram: {sorted(impares)}\n')

'''
num = [[], []]
valor = 0
for c in range(7):
  valor = int(input('Digite um valor: '))
  if valor % 2 == 0:
    num[0].append(valor)
  else:
  num[1].append(valor)      
'''