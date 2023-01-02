cd1 = '\033[1;31;40m'
cd2 = '\033[m'
nome = input('{}Digite o seu nome: {}'.format(cd1, cd2))
nome = nome.lower()
print('Silva' in nome)

'''
nome = str(input('digite o seu nome: '))
print('seu nome tem silva? {}'.format('silva' in nome.lower()))
'''
