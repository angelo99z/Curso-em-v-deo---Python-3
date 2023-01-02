cd1 = '\033[1;36m'
cd2 = '\033[m'
nome = str(input('{}Digite o seu nome completo: {}'.format(cd1,cd2))).strip()
print('{}Seu nome em maiúsculas é {}{}'.format(cd1, nome.upper(), cd2))
print('{}Seu nome em minúsculas é {}{}'.format(cd1, nome.lower(), cd2))
print('{}Seu nome tem ao todo {} letras{}'.format(cd1, len(nome)-nome.count(' '), cd2))
#print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('{}Seu primeiro nome é  {} e ele tem {} letras{}'.format(cd1, separa[0], len(separa[0]), cd2))
