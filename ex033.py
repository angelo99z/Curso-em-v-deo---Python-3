print('\ndigite 3 números: \n')
n1 = int(input())
n2 = int(input())
n3 = int(input())
'''lista = [n1, n2, n3]
lista_ordenada = sorted(lista)
print('o menor número é: {}'.format(lista_ordenada[0]))
print('o maior número é: {}'.format(lista_ordenada[2]))'''

if n1 < n2 and n1 <= n3:
    print('o menor número é: ', n1)
if n2 < n1 and n2 <= n3:
    print('o menor número é: ', n2)
if n3 < n2 and n3 < n1:
    print('o menor número é: ', n3)
else:
    print()
if n1 > n2 and n1 >= n3:
    print('o maior número é: ', n1)
if n2 > n1 and n2 >= n3:
    print('o maior número é: ', n2)
if n3 > n2 and n3 > n1:
    print('o maior número é: ', n3)
