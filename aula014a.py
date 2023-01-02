'''c = 1 
while c < 10:
  print(c)
  c +=1
print('FIM')'''

'''n = 1
while n != 0:
  n = int(input('Digite um número: '))
print('FIM')'''

'''r = 's'
while r == 's':
  n = int(input('Digite um número: '))
  r = str(input('Quer continuar? [S/N]: ')).lower()
print('FIM')'''

n = 1
par = impar = 0
while n != 0:
  n = int(input('Digite um valor: '))
  if n != 0:
    if n % 2 == 0:
      par += 1
    else:
      impar += 1 
print('Você digitou {} números pares e {} números impares'.format(par, impar))  
