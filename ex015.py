cd1 = '\033[1;35m'
cd2 = '\033[m'
km = float(input('{}Informe a quantidade de Km rodados com o carro alugado: {}'.format(cd1, cd2)))
dia = int(input('{}Informe por quantos dias o carro foi alguado: {}'.format(cd1, cd2)))
total = (dia * 60) + (km * 0.15)
print('{}O valor total do aluguel é: R${}{}\n'.format(cd1, total, cd2))
