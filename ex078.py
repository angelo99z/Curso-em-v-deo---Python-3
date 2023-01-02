numeros = []
maior = -1000
menor = 1000

for c in range(5):
  n = int(input(f'(posição {c}) Digite um número: '))
  numeros.append(n)
  if n > maior:
    maior = n
  if n < menor:
    menor = n

print(f'Você digitou os valores {numeros}')        
print(f'Maior número da lista: {maior} nas posições ', end='')
for cont, num in enumerate(numeros):
  if num == maior:
    print(f'{cont}...', end='')
print()    
print(f'Menor número da lista: {menor} nas posições ', end='')
for cont, num in enumerate(numeros):
  if num == menor:
    print(f'{cont}...', end='')
print()
print('-='*30)