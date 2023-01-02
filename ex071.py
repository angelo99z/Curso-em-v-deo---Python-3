from time import sleep
print('-=-'*15, '\n             CAIXA ELETRÔNICO\n', '-=-'*15)
nota1 = nota10 = nota20 = nota50 = 0
while True:
  saque = int(input('Qual valor deseja sacar?: R$'))
  if saque // 50 > 0:
    nota50 = saque // 50
    saque -= nota50 * 50
    print(f'Total de cédulas de R$50: {nota50}')
  if saque // 20 > 0:
    nota20 = saque // 20
    saque -= nota20 * 20
    print(f'Total de cédulas de R$20: {nota20}')
  if saque // 10 > 0:
    nota10 = saque // 10
    saque -= nota10 * 10
    print(f'Total de cédulas de R$10: {nota10}')
  if saque // 1 > 0:
    nota1 = saque // 1
    saque -= nota1 * 1
    print(f'Total de cédulas de R$1: {nota1}')
  print('-=-'*15)  
  print('\n!!!FIM!!!\n')
  break

