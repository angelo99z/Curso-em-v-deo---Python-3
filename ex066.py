s = n = c = 0
while True:
  n = int(input('Digite um número [999 para parar]: '))
  c += 1
  if n == 999:
    break
  s += n
print(f'\nForam digitados {c} números\nA soma entre eles foi {s}')
