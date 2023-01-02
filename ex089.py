from time import sleep
alunos = []
aluno = [[], [], []]
print()
while True:
  print('-='*30)
  aluno[0] = str(input('Digite o nome do aluno: '))
  aluno[1] = int(input('Digite a 1° nota: '))
  aluno[2] = int(input('Digite a 2° nota: '))
  alunos.append(aluno[:])
  aluno = [[], [], []]
  menu = str(input('Quer continuar? [S/N]: ')).lower()
  if menu == 'n':
    print('Você escolheu sair! ')
    print('-='*30)
    break

print('N°  NOME            MÉDIA')
print('- - - - - - - - - - - - - -')
for c in range(len(alunos)):
  print(f'{c}   {alunos[c][0]:<14}   {(alunos[c][1]+alunos[c][2]) / 2:>}')  
print('- - - - - - - - - - - - - -')


while True:
  menu = int(input('\nMostrar notas de qual aluno? [999 interrompe]: '))
  if menu <= len(alunos):
    print(f'\nAs notas de {alunos[menu][0]} são: [{alunos[menu][1]}] [{alunos[menu][2]}]')
    sleep(2)
    print('\nN°  NOME            MÉDIA')
    print('- - - - - - - - - - - - - -')
    for c in range(len(alunos)):
      print(f'{c}   {alunos[c][0]:<14}   {(alunos[c][1]+alunos[c][2]) / 2:>}')  
    print('- - - - - - - - - - - - - -')
  elif menu == 999:
    print('\nVocê escolheu sair')
    break
  else:
    print('\nDigite um valor válido ')
    menu = int(input('\nMostrar notas de qual aluno? [999 interrompe]: '))
    