galera =[] # lista principal onde vai conter os nomes e as idades dos usuários
dado = [] # lista de suporte para a lista principal, seus dados serão "copiados" para a lista principal e depois serão apagados para receber novos dados
totmaior = totmenor = 0 #declara os valores das variaveis total maior e total menor igual a zero ao mesmo tempo
for c in range(3):
  print('\n')
  dado.append(str(input('Nome:')))
  dado.append(int(input('Idade: ')))
  galera.append(dado[:]) # faz uma cópia dos dados da lista de suporte para a lista principal
  dado.clear() # apaga os dados da lista de suporte para receber novos dados
  
for p in galera:
  if p[1] >= 21:
    print(f'\n{p[0]} é maior de idade.')
    totmaior += 1
  else:
    print(f'\n{p[0]} é maior de idade.')
    totmenor += 1
    
print(f'\nTemos {totmaior} maiores e {totmenor} menores de idade.\n')        