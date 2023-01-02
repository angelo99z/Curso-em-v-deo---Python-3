from math import sqrt
cd1 = '\033[1;35m'
cd2 = '\033[m'
c1 = float(input('{}Insira o valor do cateto maior: {}'.format(cd1, cd2)))
c2 = float(input('{}Insira o valor do cateto menor: {}'.format(cd1, cd2)))
hip = (c1**2)+(c2**2)
r = sqrt(hip)
print('{}O valor da hipotenusa é: {:.4f}{}\n'.format(cd1, r, cd2))
