'''Crie um dicionário cujas chaves são os meses do ano e os valores são a
duração (em dias) de cada mês'''
'''Imprima as chaves seguidas dos seus valores para dicionário criado no
exercício anterior.
Exemplo:
Janeiro - 31
Fevereiro - 28
Março - 31
Etc...'''

ano = {
    'janeiro':'31 dias',
    'fevereiro' : '28 dias',
    'março' : '31 dias',
    'abril' : '30 dias',
    'maio' : '31 dias',
    'junho' : '30 dias',
    'julho' : '31 dias',
    'agosto' : '31 dias',
    'setembro': '30 dias',
    'outubro' : '31 dias',
    'novembro' : '30 dias',
    'dezembro' : '31 dias'
}

for mes in ano.keys():
    print(f'{mes}: {ano[mes]}')