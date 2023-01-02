print('\nInforme o comprimento de 3 retas em cm: \n')
r1 = float(input())
r2 = float(input())
r3 = float(input())
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
    if r1 == r2 and r1 == r3:
      print('\nTipo do triângulo: EQUILÁTERO\n')
    elif r1 == r2 or r2 == r3 or r1 == r3:
      print('\nTipo do triângulo: ISÓCELES\n')
    else:
      print('\nTipo do triângulo: ESCALENO\n')    
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')  