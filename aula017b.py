valores = list(range(4,11)) #cria uma lista com números dentro do range especificado, eliminando o último valor
print(valores)
valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort() #ordena a lista
print(valores)
valores.sort(reverse=True) #ordena a lista de tras pra frente
print(valores)
print(len(valores)) #imprime o número de itens contidos na lista
#for v in valores:
#  print(f'{v}...', end='')

valores = []
for cont in range(0, 5):
  valores.append(int(input('Digite um valor: ')))
print('Cheguei ao final da lista.')
for c, v in enumerate(valores):
  print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
