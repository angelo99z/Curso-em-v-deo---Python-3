from time import sleep
cd1 = '\033[1;35m'
cd2 = '\033[m'
print('{}informe a lagura e a altura de uma parede para calcular a quantidade necessária de tinta{}'.format(cd1, cd2))
sleep(2.5)
largura = float(input('{}Informe a \033[1;32mLARGURA\033[m {}da parede: {}'.format(cd1, cd1, cd2)))
altura = float(input('{}Informe a \033[1;32mALTURA\033[m {}da parede: {}'.format(cd1, cd1, cd2)))
total = (altura * largura) / 2
print('{}calculando...{}'.format(cd1, cd2))
sleep(2)
print('{}São necessários {:.2f} litro(s) de tinta para pintar a parede{}\n'.format(cd1, total, cd2))
