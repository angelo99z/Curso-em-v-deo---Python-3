somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulher20 = 0
for p in range(1, 5):
  print('----- {} PESSOA -----'.format(p))
  nome = str(input('Nome: ')).strip()
  idade = int(input('Idade: '))
  sexo = str(input('SexO [M/F]: '))
  somaidade += idade
  if p == 1 and sexo in 'Mm':
    maioridadehomem = idade
    nomevelho = nome
  if sexo in 'mM' and idade > maioridadehomem:
    maioridadehomem = idade
    nomevelho = nome
  if sexo in 'Ff' and idade < 20:
    totalmulher20 += 1
     
mediaidade = somaidade / 4 
print('\nA média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos\n'.format(totalmulher20))

'''
nomes = ''
idades = 0
sexos = ''
usuario = 1
for c in range(1, 5):
  print('\nUsuário {}:'.format(usuario))
  nome = str(input('Informe o nome: '))
  idade = int(input('Informe a idade: '))
  sexo = str(input('Informe o sexo (M ou F): ')).lower()
  if sexo == 'm' or sexo == 'f':
    nomes = nomes + nome
    idades = idades + idade
    sexos = sexos + sexo
    usuario += 1
  else:
    print('\n!!!Informe um valor válido (M ou F)!!!\n')
    quit()
lista_idades = [idades]    
soma = sum(lista_idades)
print('\nA média de idades é : {}'.format(soma / 4))
print('-=-'*20)
print(nomes.split())
print(sexos.split())
print('nomes: {}'.format(nomes))
print('idades: {}'.format(idades))
print('sexos: {}'.format(sexos))
'''