cd1 = '\033[1;31;40m'
cd2 = '\033[m'
cid = input('{}Digite o nome da sua cidade: {}\n'.format(cd1, cd2))
cid = cid.lower()
div = cid.split()
if div[0] == 'santo':
    print('\n{}o nome da cidade começa com Santo{}\n'.format(cd1, cd2))
else:
    print('\n{}o nome da cidade não começa com Santo{}\n'.format(cd1, cd2))

'''
cid = str(input('digite o nome de uma cidade: )).strip()
print(cid[:5].upper() == 'Santo')

'''
