print('-=-'*10, 'Digite vários números, no final será informado a média', '-=-'*10)
n = 0
c = 0
s = []
m = 'sim'
maior = 0
menor = 9999999999999999999
while m == 'sim':
  n = int(input('\nDigite um número: '))
  c += 1
  m = str(input('''\nQuer continuar? 

  [ SIM ]
  [ NAO ]
  #Opção: ''')).lower()
  s.append(n)
  if n > maior:
    maior = n
  if n < menor:
    menor = n

s = sum(s) 
print('\nA média dos números digitados é: {:.1f}'.format(s/c))
print('Menor número: {}'.format(menor))
print('Maior número: {}\n'.format(maior))