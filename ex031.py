km = float(input('informe quantos Km de viajem será percorrido pelo ônibus: '))
if km <= 200:
    p = 0.5 * km
    print('o valor da passagem é: R${:.2f}'.format(p))
else:
    p = 0.45 * km
    print('o valor da passagem é: R${:.2f}'.format(p))
