lanche = ['hamburguer', 'suco', 'pizza', 'pudim', 'pizza']
lanche.insert(0, 'hot dog') #insere um novo item a lista na posição desejada (zero nesse exemplo), a posição dos outros itens é automaticamente ajustada.
lanche.append('sorvete') #adiciona um item ao final da lista
print(lanche)
del lanche[2] #remove um item da lista pela sua posição
lanche.pop(1) #outro método para remover um item pela sua posição, se o item a ser exluído não for específicado o ultimo item é removido
lanche.remove('pizza') #remove um item da lista pelo seu nome, se o item a ser removido for repetido na lista, somente o primeiro será removido
#OBS: Após qualquer uma dessas alterações a lista é automaticamente reorganizada
print(lanche)
if 'pizza' in lanche: #verifica se um item específico está contido na lista, caso positivo o item é removido.
  lanche.remove('pizza')
  