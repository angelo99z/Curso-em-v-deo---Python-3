'''
#imprime oi 5 vezes (em laço), depois imprime 'FIM'
for c in range(1, 6):
  print('oi')
print('FIM')

'''

'''
#imprime 'oi' e 'FIM' 5 vezes (em laço)
for c in range(1,6):
  print('oi')
  print('FIM')
'''  

'''
#imprime uma contagem de 0 a 5 pulando de dois em dois
for c in range(0, 7, 2):
  print(c)
print('FIM')  
'''

'''
#imprime uma contagem de zero até o número digitado
n = int(input('Digite um número: '))
for c in range(0, n+1): # o n+1 é por que sempre a posição é contada a partir do zero, ou seja, nesse exemplo 0 - 12 imprimiria de zero a onze
  print(c)
print('FIM')
'''

'''
#pede ao usuário 3 valores: I([início]onde a contagem vai começar), f([fim]onde a contagem vai terminar) e p([passo]de quanto em quanto numeros a contagem vai pular a cada número imprimido)
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
  print(c)
print('FIM')  
'''

'''
#pede ao usuário para digitar um número 3 vezes
for c in range(0, 3):
  n = int(input('Digite um valor: '))
print('FIM')
'''

'''
# pede ao usuário para digitar um número 4 vezes, e depois faz a somatória de todos eles
s = 0
for c in range(0, 4):
  n = int(input('Digite um valor: '))
  s += n #comando simplificado de: s = s + n
print('O somatório de todos os valores foi {}'.format(s))
'''