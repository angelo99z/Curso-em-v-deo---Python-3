from math import floor
cd1 = '\033[1;35m'
cd2 = '\033[m'
n = float(input('{}Digite um número real: {}'.format(cd1, cd2)))
f = floor(n)
print('{}Resultado: {}{}'.format(cd1, f, cd2))
