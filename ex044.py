print('-=-'*20)
print('\nCondições de pagamento: \nA vista no dinheiro: 10% de desconto \nCartão 1x: 5% de desconto \nCartão 2x: preço normal \nCartão 3x ou mais: 20% de juros \n')
print('-=-'*20)
valor = float(input('informe o valor do produto: '))
print('=-='*20)
cond = int(input('\n!!!Informe a condição de pagamento!!!\nDigite um número para selecionar: \nDinheiro  a vista (1) \nCartão 1x (2) \nCartão 2x (3) \nCartão 3x ou mais (4): \n'))
print('-=-'*20)
if cond == 1:
  print('\nCondição de pagamento selecionada: A VISTA')
  print('\nValor final: R${:.2f}\n'.format(valor * 0.90))
elif cond == 2:
  print('\nCondição de pagamento selecionada: CARTÃO 1X')  
  print('\nValor final: R${:.2f}\n'.format(valor * 0.95))  
elif cond == 3:
  print('\nCondição de pagamento selecionada: CARTÃO 2X')  
  print('\nValor final: R${:.2f}\n'.format(valor))  
elif cond == 4:
  print('\nCondição de pagamento selecionada: CARTÃO 3X')  
  print('\nValor final: R${:.2f}\n'.format(valor * 1.2))  
else: 
  print('\n!!!Informe uma opção de pagamento válida!!!\n')  
  