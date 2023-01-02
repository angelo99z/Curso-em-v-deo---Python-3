print('\nDigite dois números inteiros: \n')
n1 = int(input())
n2 = int(input())
if n1 > n2:
  print('\n{} é o valor maior\n'.format(n1))
elif n2 > n1:
  print('\n{} é o valor maior\n'.format(n2))
else:
  print(('\nNão existe valor maior!!! os dois são iguais\n'))    