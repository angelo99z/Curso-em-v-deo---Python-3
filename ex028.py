'''from random import randint
import random
a = int(random.randrange(0, 6))
n = int(input('digite um valor entre 0 e 5: '))
if n == a:
    print('PARABENS!!!, você acertou!!!\n:)')
else:
    print('você errou!!! \n:(')'''

cd1 = '\033[1;32;40m'
cd2 = '\033[m'
import random
from time import sleep
cpu = random.randint(0, 5)
print('{}-=-{}'.format(cd1, cd2)*20)
print('{}O computador gerou um numero entre 0 e 5, tente adivinhar!!!{}'.format(cd1, cd2))
print('{}-=-{}'.format(cd1, cd2)*20)
player = int(input('{}Digite um número: {}'.format(cd1, cd2)))
print('{}PROCESSANDO...{}'.format(cd1, cd2))
sleep(1.5)
if player >=0 and player <=5:
    if player == cpu:
        print('{}-=-{}'.format(cd1, cd2)*20)
        print('{}PARABENS!!! Você acertou!{}'.format(cd1, cd2))
        print('{}-=-{}'.format(cd1, cd2)*20)
    else:
        print('{}-=-{}'.format(cd1, cd2)*20)
        print('{}Você errou, o número era: {}{}'.format(cd1, cpu, cd2))
        print('{}-=-{}'.format(cd1, cd2)*20)
else:
    print('{}Digite um número válido{}\n'.format(cd1, cd2))