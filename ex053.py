frase = str(input('\nDigite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)- 1, -1, -1):
  inverso += junto[letra]
print('\nO inverso de {} é {}'.format(junto, inverso))  
if inverso == junto:
  print('\nTemos um palindromo!\n')
else:
  print('\nA frase digitada não é um palindromo!\n')  