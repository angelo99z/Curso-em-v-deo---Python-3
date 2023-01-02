import random
cd1 = '\033[1;36m'
cd2 = '\033[m'
n1 = str(input('{}Informe o nome do aluno 1: {}'.format(cd1, cd2)))
n2 = str(input('{}Informe o nome do aluno 2: {}'.format(cd1, cd2)))
n3 = str(input('{}Informe o nome do aluno 3: {}'.format(cd1, cd2)))
n4 = str(input('{}Informe o nome do aluno 4: {}'.format(cd1, cd2)))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('{}Ordem de apresentação dos alunos:  {}{}\n'.format(cd1, lista, cd2))
