import csv

arquivo1 = r'alunos.csv'
arquivo2 = r'alunos_media.csv'

import shutil

shutil.copy2(arquivo1, arquivo2)

import pandas as pd

media = pd.read_csv('alunos_media.csv')
media['Media'] = ((media['Prova_1'] + media['Prova_2'] + media['Prova_3'] + media['Prova_4']) / 4)
media.to_csv('alunos_media.csv', index=False)