import random
from time import sleep
print('\n--------------------JOGO DA ADIVINHAÇÃO--------------------')
print('Tente adivinhar o número (0 a 10) que a máquina irá escolher')
sleep(1)
print('o computador está escolhendo um número...')
sleep(1.5)
numeros = [1, 2, 3, 4 , 5, 6, 7, 8, 9, 10]
cpu = random.choice(numeros)
tentativas = 0
player = int(input('Digite um número: '))
while player != cpu:
    print('---------- ### ----------\n')
    print('!!!VOCÊ ERROU!!! Tente novamente: ')
    tentativas += 1
    player = int(input('Digite um número: '))
print('\nParabéns você acertou!')
print('foram necessárias {} tentativas até acertar\n'.format(tentativas))