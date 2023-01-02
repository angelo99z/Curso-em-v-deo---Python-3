'''
def contador(i, f, p):
    '''
   #-> Faz uma contagem e mostra na tela.
    #:param i: início da contagem
    #:param f: fim da contagem
    #:param p: passo da contagem
    #:return: sem retorno
'''
    #Cria uma descrição para a função

    c = i
    while c<=f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


help(contador) #pede ao python uma descrição sobre a função "contador"
'''

def somar(a=0,b=0,c=0):
    '''
   -> Faz a soma de três valores e mostra o resultado na tela
    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: O terceiro valor
    '''
    s = a+b+c
    print(f'A soma dos valores é {s}')
    

somar(3,2)#mesmo não dando o valor para c, como foi previamente dado como zero (linha 22), o programa somou os dois valores
