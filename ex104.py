def leiaint(numero):
    while True:
        if numero.strip() == '':
            print('ERRO! Digite um número inteiro válido.')
            quit()
        if numero.isnumeric() == False:
            print('ERRO! Digite um número inteiro válido.')
            quit()
        else:
            break

n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')