from time import sleep
cd1 = '\033[1;35m'
cd2 = '\033[m'
print('{}Será dado \033[1;32m5%\033[m {}de desconto na compra{}'.format(cd1, cd1, cd2))
preco = float(input('{}Digite o preço do produto: {}'.format(cd1, cd2)))
desc = (preco * 0.95)
print('{}Calculando o desconto...{}'.format(cd1, cd2))
sleep(2)
print('{}Valor total do produto (5% de desconto): R${:.2f}{}\n'.format(cd1,desc,cd2))
