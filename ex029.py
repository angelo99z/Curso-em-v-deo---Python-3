cd1 = '\033[1;32;40m'
cd2 = '\033[m'
v = float(input('\n{}informe a velocidade(Km/h) em que o carro está: {}'.format(cd1, cd2)))
l = 80
if v > 80:
    x = (v - l) * 7
    print('\n{}velocidade acima do limite permito,{} {}VOCÊ FOI MULTADO!!!{}'.format(cd1, cd2, '\033[1;31;40m', cd2))
    print('{}valor da multa: R${:.2f}{}'.format(cd1, x, cd2))

else:
    print('\n{}velocidade abaixo do limite de velocidade!!!\nMuito bem{}'.format(cd1, cd2))
