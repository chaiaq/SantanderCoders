'''Questão 1.
Faça um programa que peça ao usuário um número e imprima todos os números de um até o
número que o usuário informar.
💡 Exemplo:
Se o usuário informar o número 5, seu programa deverá imprimir: 1 2 3 4 5.'''

numero = 1

final = int(input('Digite um número:'))
while numero <= final:
    print(numero)
    numero = numero +1