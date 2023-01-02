dados = {}                            #dicionário em python é o "{}""
dados = {'nome':'Pedro', 'idade':25}  #declarando as variáveis do dicionário
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'                     #adicionando uma nova váriavel de sexo
del dados['idade']                    #excluindo a váriavel idade
print(dados)