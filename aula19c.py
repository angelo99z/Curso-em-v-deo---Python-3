'''
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') # OBS: ao usar print formatado é preciso usar aspas duplas ao chamar um item do dicionário, pois já está
                                                           # dentro de aspas simples
                                                           
pessoas['nome'] = 'Angelo' #substitui o valor da variável nome
for k, v in pessoas.items(): #funciona de forma igual ao comando "enumerate"
  print(f'{k} = {v}')'''
  
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]) 
print(brasil[0]['uf'])
print(brasil[1]['sigla'])