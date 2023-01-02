from time import sleep
cd1 = '\033[1;35m'
cd2 = '\033[m'
print('\n\033[1;32m!!!PARABENS!!!\033[m \n{}Você recebeu um aumento de 15% no seu salário{}'.format(cd1, cd2))
sal = float(input('{}Digite o seu salário em R$: {}'.format(cd1, cd2)))
aum = sal * 1.15
print('{}Calculando seu novo salário...{}'.format(cd1, cd2))
sleep(2)
print('{}Seu novo salário é: \033[1;32mR${:.2f}{}\033[m\n'.format(
    cd1, aum, cd2))
