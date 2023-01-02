numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte' )
n = int(input('Digite um número entre 0 e 20: '))
while True:
  if n >=0 and n <=20:
    print(f'Voce digitou o número {numeros[n]}\n')
    break
  else:
    print('Tente novamente. Digite um número entre 0 e 20: ')
    n = int(input('Digite um número entre 0 e 20: '))
