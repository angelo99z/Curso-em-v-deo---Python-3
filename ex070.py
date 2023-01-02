from time import sleep
print('-=-'*15, '\n          ESTATÍSTICAS EM PRODUTOS\n', '-=-'*15)
preco = total = maisdemil = 0
maisbarato = 99999999999
nomemaisbarato = nome = ''
while True:
  print('---'*15)
  print('Cadastre um produto:')
  nome = str(input('Produto: '))
  preco = float(input('Preço: '))
  print('---'*15)
  total += preco
  if preco > 1000:
    maisdemil += 1 
  if preco < maisbarato:
    maisbarato = preco
    nomemaisbarato = nome
  opcao = str(input('Quer adicionar mais um produto[S/N]?: ')).lower()
  if opcao == 'n':
    print('Você escolheu sair')
    sleep(0.8)
    print('Saindo....')
    sleep(1.2)
    break

print('-=-'*15)
print('Total da compra: R${:.2f}'.format(total))
print(f'Foi comprado {maisdemil} produtos custando mais de R$1000.00')
print('O produto mais barato foi o/a {} que custou R${:.2f}'.format(nomemaisbarato, maisbarato))    
print('\n!!!FIM!!!\n')