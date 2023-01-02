from math import sqrt
cd1 = '\033[1;36m'
cd2 = '\033[m'
n = float(input('{}digite um número: {}'.format(cd1, cd2)))
dobro = n * 2
triplo = n * 3
raiz = sqrt(n)
print('{}Dobro: {}{}'.format(cd1, dobro, cd2))
print('{}Triplo: {}{}'.format(cd1, triplo, cd2))
print('{}Raiz quadrada: {}{}'.format(cd1, raiz, cd2))
