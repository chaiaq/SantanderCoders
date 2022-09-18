'''Para os exercícios 1 ao 3, você precisará do arquivo: alunos.csv. Clique aqui
para baixá-lo (ao salvar, renomeie o arquivo).
1 - Neste exercício você deve criar um programa que abra o arquivo
"alunos.csv" e imprima o conteúdo do arquivo linha a linha.
Note que esse é o primeiro exercício de uma sequência, então o seu código
pode ser reaproveitado nos exercícios seguintes. Dito isso, a recomendação é
usar a biblioteca CSV para ler o arquivo mesmo que não seja realmente
necessário para esse primeiro item.'''

import csv
with open('alunos.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)