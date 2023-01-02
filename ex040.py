n1 = float(input('\nInforme a nota da prova 1: '))
n2 = float(input('\nInforme a nota da prova 2: '))
m = (n1 + n2) / 2
print('\nSua média é {}'.format(m))
if m < 5:
  print('\nVocê está REPROVADO\n')
elif m >= 5 and m <7:
  print('\nVocê está em RECUPERAÇÃO\n')
else:
  print('\nVocê está APROVADO\n')  
  