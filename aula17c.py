a = [2, 3, 4, 7]
b = a  #lista B recebe os mesmos valores da lista A
b[2] = 8  #ao alterar um valor da lista B, a lista A também é alterada, pois as listas A e B foram vinculadas uma a outra na linha 2
print(f'Lista A: {a}')
print(f'Lista B: {b}') #perceba que as duas listas geram valores iguais

#----------------------------------------------------------------------------------------------------------------------------------------
a = [2, 3, 4, 7]
b = a[:] #lista B recebe uma cópia dos itens da lista A, desta forma as listas não são vinculadas
b[2] = 8 #desta forma é possível alterar os itens da lista B sem interferir na lista A
print(f'Lista A: {a}')
print(f'Lista B: {b}') 