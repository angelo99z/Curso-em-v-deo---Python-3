'''
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(7)
print(f'Os resultados foram {r1}, {r2} e {r3}')
'''

'''
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input(f'Digite um número: '))
print(f'O fatorial de {n} é {fatorial(n)}')
'''

def par(n=0):
    if n%2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
