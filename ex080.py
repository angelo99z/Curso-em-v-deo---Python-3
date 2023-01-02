numeros = []
for c in range(5):
  n = int(input('Digite um número: '))
  if c == 0:
    print('Valor adicionado ao final da lista!')
    numeros.append(n)
  elif n > numeros[-1]:
    numeros.append(n)
    print('Valor adicionado ao final da lista!')
  else:
    pos = 0
    while pos < len(numeros): # enquanto a pos não chegar ao final da lista...
      if n <= numeros[pos]:  #...compara o número atual com os número já existentes na lista, se o número atual for menor ou igual...
        numeros.insert(pos, n) #... o número é inserido na posição "pos" que aumenta a cada 
        print(f'Valor adicionado na posição {pos}')
        break
      pos += 1
print('-='*30)
print(f'Lista ordenada: {numeros}')        
    