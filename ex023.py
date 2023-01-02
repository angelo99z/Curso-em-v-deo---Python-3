cd1 = '\033[1;36m'
cd2 = '\033[m'
n = input('{}Digite um número entre 0 e 9999: {}'.format(cd1, cd2))
div = n.split()
print('{}Unidade: {}{}'.format(cd1,div[0][3], cd2 ))
print('{}Uezena:  {}{}'.format(cd1, div[0][2], cd2))
print('{}Centena: {}{}'.format(cd1, div[0][1], cd2))
print('{}Milhar:  {}{}\n'.format(cd1, div[0][0], cd2))

'''
n = int(input('digite um número: '))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num //100 %10
mil = num // 1000 %10 
print('unidade {}'.format(uni))
print('dezena  {}'.format(dez))
print('centena {}'.format(cen))
print('milhar  {}'.format(mil))
'''
