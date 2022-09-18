import csv

with open('alunos.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)
        
'''2 - Para o segundo exercício, você deve criar um programa que realize uma
cópia do arquivo "alunos.csv". Essa cópia deve ser um arquivo chamado
"alunos_copia.csv".'''

import shutil
arquivo1 = r'alunos.csv'
arquivo2 = r'alunos_copia.csv'

shutil.copy2(arquivo1, arquivo2)