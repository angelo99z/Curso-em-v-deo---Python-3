cd1 = '\033[4;34m'
cd2 = '\033[m'
print('digite dois números: \n')
n1 = int(input())
n2 = int(input())
soma = n1 + n2
print('{}A soma dos números é:\n{}{}'.format(cd1, soma,cd2))