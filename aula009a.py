frase = '   Curso em Video Python   '
print(frase[3:13])  # mostra a frase do caractere 3 ao 13
print(frase[:13])  # mostra a frase do 1°caractere (0) ao 13
print(frase[3:])   # mostra a frase do caractere 3 ao ultimo
print(frase[3:13:2])
# mostra a frase do caractere 3 ao 13 pulando de dois em dois
print(frase[::2])
# mostra a frase do 1° caractere ao ultimo pulando de dois em dois

# print('''Flash bang
# White screen
# No field of vision
# Cant see what you cant hear in the distance
# Concussed, your head bust
# I scope you like its 1v1 on rust I keep that thang tucked its Fukkit cannot let you up''')

print(frase.count('o'))
# conta no número de vezes que a frase tem o carctere "o" (minúsculo)
print(frase.count('O'))
# conta no número de vezes que a frase tem o carctere "O" (maiúsculo)
print(frase.upper())  # imprime a frase tudo em miúsculo
print(frase.lower())  # imprime a frase tudo em minúsculo
print(len(frase))  # conta no número de caracteres que a frase tem
print(len(frase.strip()))
# conta o número de caracteres que a frase tem sem espaços
print(frase.replace('Python', 'Android'))
# substitui uma palavra da frase por outra nesta instância
print(frase)
frase = frase.replace('Python', 'Android')
# substiui uma palavra por outra e salva, ao printar depois é possível ver que foi salvo
print(frase)
print('Curso' in frase)
# verifica se a palavra "Curso" (OBS: Tem case sensetive) está contida na "frase" com True ou False
print(frase.find('Video'))
# aponta a posição em que começa a palavra "Video", se retornar -1 é pq a palavra não contém na frase
print(frase.lower().find('Video'))
# faz a mesma coisa do código anterior porém antes disso deixa toda a frase minúscula
print(frase.split())  # imprime na tela as palavras da frase separados em uma lista
dividido = frase.split()  # cria um objeto com o comando para dividir a frase
print(dividido[0])
# imprime uma palavra em específico da frase a partir da sua posição
print(dividido[2][3])  # imprime a letra de posição 3 na palavra de posição 2
