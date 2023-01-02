idade = int(input('\nInforme a sua idade: '))
if idade <=9:
  print('\nCategoria MIRIM\n')
elif idade > 9 and idade <=14:
  print('\nCategoria INFANTIL\n')
elif idade > 14 and idade <=19:
  print('\nCategoria JUNIOR\n')
elif idade > 19 and idade <=20:
  print('\nCategoria SÊNIOR\n')
else:
  print('\nCategoria MASTER\n')     
   