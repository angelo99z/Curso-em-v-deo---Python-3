n = int(input('digite um número: '))
fat = 1
i = 2
while i <= n:
  fat = fat * i
  i += 1
print ('\nO fatorial de {} é: {}\n'.format(n, fat))