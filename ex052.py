n = int(input('\nDigite um número inteiro: '))
x = 2
y = 0
for c in range(1, 11):
  if n % x == 0:
    y += 1
    x += 1
if n == 2:
  print('\n!!!Este número é primo!!!\n') 
elif y > 0:
  print('\n!!!Este número não é primo!!!\n') 
else:
  print('\n!!!Este número é primo!!!\n')       
    