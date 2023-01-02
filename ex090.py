dic = {} 
dic['nome'] = str(input('\nNome: '))
dic['média'] = int(input('Média: '))
if dic['média'] < 50:
  dic['situação'] = 'Reprovado'
elif dic['média'] <70 >50:
  dic ['situação'] = 'Recuperação'
else:
  dic['situação'] = 'Aprovado' 

print('-='*15)
print(f'Nome é igual a {dic["nome"]}')
print(f'Média é igual a {dic["média"]}')
print(f'Situação é igual a {dic["situação"]}')
print('-='*30)
