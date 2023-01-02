print('\n{}CALCULADORA DE IMC{}'.format('-='*15, '-='*15))
peso = float(input('\nInforme o seu PESO em KG: '))
alt = float(input('\nInforme a sua altura em Metros (ex: 1.80): '))
imc = peso / (alt * alt)
print('\nSeu IMC é: {:.2f}'.format(imc))
if imc < 18.5:
  print('\n!!!Você está ABAIXO do peso!!!')
elif imc > 18.5 and imc <=25:
  print('\nPeso IDEAL')  
elif imc >25 and imc <= 30:
  print('\nVocê está em SOBREPESO')  
elif imc > 30 and imc <=40:
  print('Você está em OBESIDADE')
elif peso <=0:
  print('\nDigite um peso acima de ZERO')  
else:
  print('\n!!!CUIDADO!!!\nVocê está em OBESIDADE MÓRBIDA')  
  