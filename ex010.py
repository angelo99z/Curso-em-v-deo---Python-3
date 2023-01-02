from time import sleep
cd1 = '\033[1;34m'
cd2 = '\033[m'
r = float(input('{}Digite o valor da carteira em real brasileiro(R$): {}'.format(cd1, cd2)))
d = r / 3.5
print('{}Convertendo em Dólar...{}'.format(cd1, cd2))
sleep(1.5)
print('{}Valor em dólar(U$): ${:.2f}{}'.format(cd1, d, cd2))
