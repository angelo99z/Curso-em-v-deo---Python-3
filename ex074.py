import random
lista = []
tupla = 0
aleatorio = 0
for c in range(5):
  aleatorio = int(random.randrange(0, 100))
  lista.append(aleatorio)
  
tupla = lista[0], lista[1], lista[2], lista[3], lista[4]
print('-='*15)
print('Tupla:')
print(tupla)
tupla = sorted(tupla)
print(f'Menor: {tupla[0]}')
print(f'Maior: {tupla[4]}')
print('-='*15)