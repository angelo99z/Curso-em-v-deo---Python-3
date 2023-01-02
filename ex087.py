'''
matriz = []
linha1 = []
linha2 = []
linha3 = []
pares = []
cont = 0
c3_soma = []
maior = 0

for c in range(3):
  n = int(input(f'Digite um valor para [0, {c}]: '))
  linha1.append(n)
  if n % 2 == 0:
    pares.append(n)
  if c == 2:
    c3_soma.append(n)
      
for c in range(3):
  n = int(input(f'Digite um valor para [0, {c}]: '))
  linha2.append(n) 
  if n % 2 == 0:
    pares.append(n)
  if c == 2:
    c3_soma.append(n)
  if n >= maior:
    maior = n  
    
    
for c in range(3):
  n = int(input(f'Digite um valor para [0, {c}]: '))
  linha3.append(n)
  if n % 2 == 0:
    pares.append(n)
  if c == 2:
    c3_soma.append(n)   
    
print()  
for c in range(3):
  print(f'[   {linha1[c]}   ]', end='')
print()  
for c in range(3):
  print(f'[   {linha2[c]}   ]', end='')
print()  
for c in range(3):
  print(f'[   {linha3[c]}   ]', end='')
print()  

print()
print(f'A soma dos valores pares é {sum(pares)}.')
print(f'A soma dos valores da terceira coluna é {sum(c3_soma)}.')
print(f'O maior valor da segunda linha é {maior}.')
print()
'''

matriz = [[0, 0, 0],[0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0 # spar(soma dos pares), mai(maior), scol(soma coluna)
for l in range(3): 
  for c in range(3):
    matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}] : '))
    
print('-=' * 30)
for l in range(3):
  for c in range(3):
    print(f'[{matriz[l][c]:^5}]', end='') 
    if matriz[l][c] % 2 == 0:
      spar += matriz[l][c]
  print()

print('-=' * 30)
print(f'A soma dos valores pares é {spar}')

for l in range(3):
  scol += matriz[l][2]
print(f'A soma dos valores da 3° coluna é {scol}')

for c in range(3):
  if c == 0:
    mai = matriz[1][c]
  elif matriz[1][c] > mai:
    mai = matriz[1][c]
print(f'O maior valor da 2° linha é {mai}')      