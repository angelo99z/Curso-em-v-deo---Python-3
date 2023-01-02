nn = int(input('informe a quantidade de nome/sobrenomes (máximo 5): '))
if nn == 1:
    nome = input('digite o seu nome completo (inserir apenas 1): ')
    print('maiúsculo: ', nome.upper())
    print('minúsculo: ', nome.lower())
    div = nome.split()
    n1 = len(div[0][0:])
    total = n1
    print('total de letras: {}'.format(total))
    print('primeiro nome: ', div[0])
if nn == 2:
    nome = input('digite o seu nome completo (inserir apenas 2): ')
    print('maiúsculo: ', nome.upper())
    print('minúsculo: ', nome.lower())
    div = nome.split()
    n1 = len(div[0][0:])
    n2 = len(div[1][0:])
    total = n1 + n2
    print('total de letras: {}'.format(total))
    print('primeiro nome: ', div[0])
if nn == 3:
    nome = input('digite o seu nome completo (inserir apenas 3): ')
    print('maiúsculo: ', nome.upper())
    print('minúsculo: ', nome.lower())
    div = nome.split()
    n1 = len(div[0][0:])
    n2 = len(div[1][0:])
    n3 = len(div[2][0:])
    total = n1 + n2 + n3
    print('total de letras: {}'.format(total))
    print('primeiro nome: ', div[0])
if nn == 4:
    nome = input('digite o seu nome completo (inserir apenas 4): ')
    print('maiúsculo: ', nome.upper())
    print('minúsculo: ', nome.lower())
    div = nome.split()
    n1 = len(div[0][0:])
    n2 = len(div[1][0:])
    n3 = len(div[2][0:])
    n4 = len(div[3][0:])
    total = n1 + n2 + n3 + n4
    print('total de letras: {}'.format(total))
    print('primeiro nome: ', div[0])
if nn == 5:
    nome = input('digite o seu nome completo (inserir apenas 5): ')
    print('maiúsculo: ', nome.upper())
    print('minúsculo: ', nome.lower())
    div = nome.split()
    n1 = len(div[0][0:])
    n2 = len(div[1][0:])
    n3 = len(div[2][0:])
    n4 = len(div[3][0:])
    n5 = len(div[4][0:])
    total = n1 + n2 + n3 + n4 + n5
    print('total de letras: {}'.format(total))
    print('primeiro nome: ', div[0])
if nn >= 6 or nn <= 0:
    print('insira um valor entre 1 e 5')
