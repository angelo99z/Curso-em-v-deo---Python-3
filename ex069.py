from time import sleep
print('-=-'*15, '\n         ANÁLISE DE DADOS DO GRUPO\n', '-=-'*15)
c = mulher20 = nhomem = mais18 = 0
while True:
  c +=1
  print(f'Pessoa {c}:')
  idade = int(input('Idade: '))
  sexo = str(input('Sexo [F/M]: ')).lower()
  if idade >=18:
    mais18 += 1
  if sexo == 'm':
    nhomem += 1
  if sexo == 'f' and idade < 20:
    mulher20 += 1
  opcao = str(input('\nQuer continuar [S/N]?: ')).lower() 
  if opcao == 'n':
    print('Você escolheu SAIR ')
    sleep(0.8)
    print('Saindo...')
    sleep(1.2)
    break
  if opcao == 's':
    print('Você escolheu continuar...\n')
    sleep(0.8)
print('-=-'*15)
print(f'\nAo todo: \n* {mais18} pessoa/s com mais de 18 anos foram cadastrados\n* {nhomem} homem/s foram cadastrados \n* {mulher20} mulher/es com menos de 20 anos foi cadastrada')
print('\n!!!FIM!!!\n')