from time import sleep
cd1 = '\033[1;31m'
cd2 = '\033[m'
m = float(input('\n{}Digite uma medida em metros: {}'.format(cd1, cd2)))
cm = m * 100
mm = m * 1000
print('{}Convertendo...{}'.format(cd1, cd2))
sleep(1.5)
print('{}cm: {}\nmm: {}{}\n'.format(cd1, cm, mm, cd2))
