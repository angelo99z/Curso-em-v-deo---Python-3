def area(larg, comp):
  print(f'\nA área do seu terreno {larg}m *{comp}m é de {larg * comp:.1f}m² \n')
  

print()  
print('-'*30)
print('Controle de Terrenos')
print('-'*30)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)  
