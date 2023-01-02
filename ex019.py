import random
cd1 = '\033[1;35m'
cd2 = '\033[m'
n1 = str(input('{}Informe o nome do aluno 1: {}'.format(cd1, cd2)))
n2 = str(input('{}Informe o nome do aluno 2: {}'.format(cd1, cd2)))
n3 = str(input('{}Informe o nome do aluno 3: {}'.format(cd1, cd2)))
n4 = str(input('{}Informe o nome do aluno 4: {}'.format(cd1, cd2)))
lista = [n1, n2, n3, n4]
r = random.choice(lista)
print('{}O aluno sorteado é {}{}\n'.format(cd1, r, cd2))
