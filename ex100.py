from random import randint
from time import sleep
numeros = []

def sorteia(lista):
    for c in range(5):
        lista.append(randint(1,10))
def somaPar(lista):
    s = 0
    for n in lista:
        if n % 2 == 0:
            s += n
    print(f'Somando os valores pares de {numeros}, temos {s}')

sorteia(numeros)
print(f'Sorteando 5 números:  {numeros}  PRONTO!')
somaPar(numeros)

