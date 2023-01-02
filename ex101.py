def vota(nascimento):
    from datetime import date
    ano = date.today().year
    idade = ano - nascimento
    if idade < 16:
        print(f'com {idade}: VOTO NEGADO')
    elif 16 <= idade <18 or idade >65:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')


ano = int(input('Ano de nascimento: '))
vota(ano)