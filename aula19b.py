filme = {'titulo': 'Star Wars',
      'ano': 1977,
      'diretor': 'George Lucas'
}

print(filme.values())      #imprime somente os "valores" do dicionário 
print(filme.keys())        #imprime somente as "chaves" do dicionário
print(filme.items())       #imprime todos os dados do dicionário
for k, v in filme.items():
  print(f'O {k} é {v}')
  