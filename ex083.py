exp = str(input('\nDigite uma expressão: '))
pilha = []

for simb in exp:
  if simb == '(':
    pilha.append('(')
  elif simb == ')':
    if len(pilha) > 0:
      pilha.pop()
    else:
      pilha.append(')')
      break
    
if len(pilha) == 0:
  print('\nSua expressão está válida!!!\n')
else:
  print('\nSua expressão está inválida!!!\n')  


      
'''
exp = str(input('Digite uma expressão: '))
abrep = exp.count('(')
fechap = exp.count(')')
lista_exp = []

if abrep == fechap:
  print('\nSua expressão está correta!!!\n')

else:
  print('\nSua expressão está incorreta!!!\n')
'''