from time import sleep
cd1 = '\033[1;35m'
cd2 = '\033[m'
g = float(input('{}Digite uma temperatura em graus C°:{} '.format(cd1, cd2)))
print('{}Temperatura sendo convertida...{}'.format(cd1, cd2))
f = (g * 1.8) + 32
print('{}Temperatura em Farenheit: {:.1f}{}'.format(cd1, f, cd2))