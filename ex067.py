print('-=-'*10, 'TABUADA', '-=-'*10)
c = 1
while True:
  n = int(input('\nDigite um número (negativo para sair): '))
  if n < 0:
    break
  while c <=11:
    t = n*1, n*2, n*3, n*4, n*5, n*6, n*7, n*8, n*9, n*10
    print(f'{n} x {c} = {t[c-1]}')
    c += 1
    if c == 11:
      c = 1
      break
print('\n!!!FIM!!!\n')    