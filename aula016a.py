'''
lanche = 'Hamburger', 'suco', 'pizza', 'pudim'
print(lanche)
print(lanche[1])
print(lanche[-1]) #imprime o item da ultima posição da tupla
print(lanche[1:3]) #ignora o item da posição zero e imprime o restante (2 e 3)
print(lanche[-3:]) 
#OBS: TUPLAS SÃO IMUTAVEIS (NÃO PODEM SER ALTERADAS)
'''


#3 formas diferentes de fazer a mesma coisa:
lanche = 'Hamburger', 'suco', 'pizza', 'pudim', 'batata frita'
#maneira 1:
for comida in lanche:
  print(f'Eu vou comer {comida}')

#maneira 2:
for cont in range(0, len(lanche)):
  print(f'Eu vou comer {lanche[cont]} na posição {cont}') #desta forma é possível mostrar o item e a posição usando este método (neste exemplo "for count in...)

#maneira 3:
for pos, comida in enumerate(lanche):
  print(f'Eu vou comer {comida} na posição {pos}') #maneira alternativa de fazer a maneira 2 usando "enumerate"
print('\nComi muito\n')



#lanche = 'Hamburger', 'suco', 'pizza', 'pudim', 'batata frita'
#print(sorted (lanche)) #printa a tupla de forma ordenada em uma LISTA

'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a 
print(c) #imprime a tupla B e A juntas, exibindo primeiro a tupla B por ser digitada primeiro
print(c.count(5)) #imprime o número de vezes que a tupla contem o "5" 
print(c.index(3)) #imprime o número a posição de "3" na tupla C, em caso de ter dois itens iguais como no caso, só é exibido a posição da primeira
print(c.index(5, 1)) #imprime o número da posição de "5" na tupla C a partir da posição 1 (8)
'''

pessoa = ('Angelo', 22, 'M', 88.6) #É possível criar uma tupla com diferentes tipos de variáveis, ex: int, float, str
del(pessoa) #apaga a tupla "pessoa"
print(pessoa) #como a tupla foi apagada ao executar ocorre um erro