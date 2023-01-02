num = int(input('Digite um número inteiro: '))
print(''' Escolhar uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
  print('{} convertido para BINÁRIO é igual a: {}\n'.format(num, bin(num)[2:]))
elif opção == 2:
  print('{} convertido para OCTAL é igual a: {}\n'.format(num, oct(num)[2:]))
elif opção == 3:
  print('{} convertido para HEXADECIMAL é igual a: {}\n'.format(num, hex(num)[2:]))
else:
  print('!!!Opção inválida!!!, Tente novamente\n')  