'''
def soma(a, b):
  print(f'A = {a} e B={b}')
  s = a + b
  

#Programa prinicipal
soma(4,5)
soma(2,6)
soma(7,3)
soma(b=4,a=10)
'''


'''
def contador(*num):
  print(f'Recebi os valores {num} e são ao todo {len(num)} números')

  
contador(2,1,5)
contador(7,10,0,9)
contador(4,6,3,5,8,2)
'''


'''
def dobra(lst):
  pos = 0
  while pos < len(lst):
    lst[pos] *=2
    pos +=1
  
  
valores = [6,3,9,1,0,2]
dobra(valores)
print(valores)
'''

def soma(* valores):
  s = 0
  for num in valores:
    s += num
  print(f'Somando os valores {valores} temos {s}')
  
  
soma(5,2)
soma(2,9,4)
