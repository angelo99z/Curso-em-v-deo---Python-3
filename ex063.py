'''
from time import sleep
print('\n')
print('-=-'*5, 'SEQUÊNCIA DE FIBONACCI', '-=-'*5)
c = int(input('Digite quantos números da sequência de Fibonacci deseja imprimir: \n'))
n1 = 0
n2 = 0
n3 = 0
print('-=-'*15)

if c <= 0:
  print('-=-'*5, '!!!FIM!!!', '-=-'*5)
  quit()  
elif c == 1:
  print(n1)  

elif c == 2:
    print(n1) 
    n1 += 1
    print(n1)
    print('-=-'*5, '!!!FIM!!!', '-=-'*5)
    quit()

elif c == 3:
  print(n1) 
  n1 += 1
  print(n1)
  n2 = n1
  print(n1)
  print('-=-'*5, '!!!FIM!!!', '-=-'*5)
  quit()

print(n1) 
n1 += 1
print(n1)
n2 = n1
print(n1)
print(n1 + n2)
n1 = n1 + n2
c -= 4

while c > 0:
  n3 = n1
  n1 = n1 + n2
  n2 = n2 + n2
  print(n1)
  n2 = n3
  c -= 1

print('-=-'*5, '!!!FIM!!!', '-=-'*5)'''

print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos deseja imprimir? '))
t1 = 0
t2 = 1
print('~'*(n*5))
print('{} > {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
  t3 = t1 + t2
  print(' > {}'.format(t3), end='')
  t1 = t2
  t2 = t3
  cont += 1
print('> FIM')
print('~'*(n*5))