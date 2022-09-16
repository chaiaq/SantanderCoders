'''Faça um programa que olhe todos os itens de uma lista e diga quantos deles
são pares.'''

lista = []

print(len(lista))

while len(lista) <= 5:
    numero = int(input("Digite um numero "))
    lista.append(numero)
    
for par in lista:
    if par % 2 == 0:
        print(par)