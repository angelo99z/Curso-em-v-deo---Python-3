from time import sleep
cd1 = '\033[1;33m'
cd2 = '\033[m'
n = int(input('{}Digite um número inteiro: {}'.format( cd1, cd2)))
print('{}Gerando a tabuada...{}'.format(cd1, cd2))
sleep(1.5)
tab = n*1, n*2, n*3, n*4, n*5, n*6, n*7, n*8, n*9, n*10
print('{}tabuada: \n{}{}\n'.format(cd1, tab, cd2))
