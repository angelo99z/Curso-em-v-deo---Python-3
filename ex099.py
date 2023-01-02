from time import sleep
def encontra_maior(* num):
    maior = 0
    print('Analizando os valores passados...')
    for c in num:
        print(f'{c}', end=' ')
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo.')
    for m in num:
        if m == 0:
            maior = m
        else:
            if m > maior:
                maior = m
    print(f'O maior valor informado foi {maior}')
    print('-='*30)
print('-=' * 30)
encontra_maior(2,3,9)
encontra_maior(3,-7,2,-5)
encontra_maior(7)
encontra_maior()