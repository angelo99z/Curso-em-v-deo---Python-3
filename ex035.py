print('\ninforme o valor de 3 medidas em cm: \n')
l1 = float(input())
l2 = float(input())
l3 = float(input())
lista = [l1, l2, l3]
lista = sorted(lista)
if lista[0] + lista[1] > lista[2]:
    print('\né possível formar um triangulo!\n')
else:
    print('\nnão é possível formar um triangulo!\n')

'''
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')    
'''
