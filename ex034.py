sal = float(input('\ninforme o seu salário: \n'))
print('analisando o seu aumento...')
if sal <= 1250:
    aum = sal * 1.15
    print('seu salário com o aumento é: R${:.2f}'.format(aum))
else:
    aum = sal * 1.10
    print('seu salário com o aumento é: R${:.2f}'.format(aum))

'''
sal = float(input('\ninforme o seu salário: \n'))
print('analisando o seu aumento...')
if sal <= 1250:
    aum = sal + (sal * 15 / 100)
    print('seu salário com o aumento é: R${:.2f}'.format(aum))
else:
    aum = sal + (sal * 10 / 100)
    print('seu salário com o aumento é: R${:.2f}'.format(aum))
'''
