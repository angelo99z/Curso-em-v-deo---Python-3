'''
teste = []
teste.append("Gustavo")
teste.append(40)  
galera = []
galera.append(teste[:]) # a lista gelera recebe uma cópia de todos os itens da lista teste
teste[0] = "maria"
teste[1] = 22
galera.append(teste[:]) # adiciona os novos valores da lista teste na lista galera
print(galera)'''


galera = ['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]
#print(galera[0])
#print(galera[0][0])
#print(galera[2][1])
for p in galera:
  print(f'{p[0]} tem {p[1]} anos de idade')


