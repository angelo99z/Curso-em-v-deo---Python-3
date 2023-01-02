nome = 'angelo'
cores = {
'limpa': '\033[m',
'azul': '\033[34m',
'amarelo': '\033[33m',
'pb': '\033[7;30m'
}
print('\nOlá muito prazer em te conhecer, {}{}{}!!!\n'.format(cores['azul'], nome, cores['limpa']))
