from time import sleep
print('\nSIMULADOR DE EMPRÉSTIMO\n')
casa = int(input('Informe o valor da casa: '))
sal = int(input('\nInforme o seu salário mensal: '))
t = int(input('\nInforme em quantos anos deseja quitar o empréstimo: '))
print('\nO valor das parcelas não pode ser maior que 30% do seu salário (R${})'.format(sal*0.3))
parcela = casa / (t*12)
sleep(1.5)
print('\nValor da parcela R${:.2f}'.format(parcela))
sleep(1)
if parcela > sal * 0.3:
  print('\n!!!Emprestimo negado!!!\n')
else:
  print('\n!!!Emprestimo aprovado!!!\n')  