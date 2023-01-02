print('\n!!!Informe o peso de 5 Pessoas!!!\n')
maior = 0
menor = 0
lista = []
for c in range(1, 6): 
  peso = float(input('Digite um peso(Kg): '))
  lista.append(peso)
lista.sort()  
print('Menor peso: {:.2f}Kg'.format(lista[0]))
print('Maior peso: {:.2f}Kg'.format(lista[4]))