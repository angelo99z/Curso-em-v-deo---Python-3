lista = []
tupla = 0
num3 = 0
pares = []
for c in range(4):
  n = int(input('Digite um número: '))
  lista.append(n)
  if n == 3:
    num3 = c +1
  if n % 2 == 0:
    pares.append(n)
        
tupla = lista[0], lista[1], lista[2], lista[3]  
print('-='*15)
print('O número 9 apareceu {} vez(es)'.format(lista.count(9)))

if 3 in lista:
  print(f'O número 3 foi digitado pela primeira vez na posição {num3}')
else:
    print('O número 3 não foi digitado nenhuma vez')

print(f'Os números pares foram: {pares}\n')    
    