ano = int(input('\nInforme o seu ano de nascimento: '))
idade = 2021 - ano
if idade <18:
  print('\nAinda não está na hora de se alistar (faltam {} anos)\n'.format(18 - idade))
elif idade == 18:
  print('\nJá está na hora de se alistar!!!\n')
else:
  print('\nJá passou da hora de se alistar (passaram {} anos)\n'.format(idade - 18))  
  