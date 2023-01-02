'''from types import new_class


frase = str(input('digite uma frase qualquer: \n')).strip()
frase = frase.lower()
n = frase.count('a')
primeira = frase.find('a')
print('a letra "a" aparece {} vezes na frase'.format(n))
print('a letra "a" aparece pela primeira vez na posição: {}'.format(primeira))'''

cd1 = '\033[1;31;40m'
cd2 = '\033[m'
frase = str(input('{}Digite uma frase: {}'.format(cd1, cd2))).lower().strip()
print('{}A letra "A" aparece {} vezes na frase{}'.format(cd1, frase.count('a'), cd2))
print('{}A primeira letra "A" apareceu na posição {}{}'.format(cd1, frase.find('a')+1, cd2))
print('{}A última letra "A" apareceu na posição {}{}\n'.format(cd1, frase.rfind('a')+1, cd2))
