cd1 = '\033[1;31;40m'
cd2 = '\033[m'
n = str(input('{}Digite o seu nome: {}'.format(cd1, cd2))).strip()
nome = n.split()
print('{}Seu primeiro nome é: {}{}'.format(cd1, nome[0], cd2))
print('{}Seu ultimo nome é: {}{}\n'.format(cd1, nome[len(nome)-1], cd2))
