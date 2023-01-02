print('\n-=-==-==-==-=-=Digite vários números e quando desejar sair, digite "999"-=-==-==-==-=-=')
n = 0
c = -1
s = []
while n != 999:
  c += 1
  n = int(input('Digite um número: '))
  s.append(n)
s = sum(s)  
print('Foram digitados {} números!\n'.format(c))
print('A soma dos números digitados é: {}'.format(s - 999))

'''
n = cont= soma = 0 # comando para que as 3 variaveis (n, cont e soma) recebam zero em uma só linha.
n = int(input('Digite um número: '))
while n != 0:
  soma += n
  cont += 1
  n = int(input('Digite um número: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))  
'''