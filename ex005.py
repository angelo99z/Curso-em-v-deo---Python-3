cd1 = '\033[1;35m'
cd2 = '\033[m'
n = int(input('{}digite um número inteiro: {}'.format(cd1, cd2)))
print('{}Sucessor: {}\nAntecessor: {}{}'.format(cd1,n+1, n-1, cd2 ))