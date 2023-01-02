from time import sleep
def contagem(inicio, fim, passo):
    if inicio > fim:
        while inicio >= fim:
            print(f'{inicio}', end=' ')
            sleep(0.3)
            inicio = inicio - passo
        print('FIM!')
        print('-=' * 30)
    else:
        while inicio <= fim:
            print(f'{inicio}', end=' ')
            sleep(0.3)
            inicio += passo
        print('FIM!')
        print('-=' * 30)

print('-='*30)
print('Contagem de 1 até 10 de 1 em 1')
contagem(1, 10, 1)

print('Contagem de 10 até 0 de 2 em 2')
contagem(10, 0 , 2)

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if passo == 0:
    passo = 1
elif passo < 0:
    passo = passo * (-1)
contagem(inicio, fim, passo)