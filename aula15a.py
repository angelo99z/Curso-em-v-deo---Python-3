'''
n = s = 0
while True:
  n = int(input('Digite um número: '))
  if n == 999:
    break
  s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}')
'''

nome = 'José'
idade = 23
salario = 987.35
print(f'O {nome} tem {idade} anos e recebe R${salario}')
