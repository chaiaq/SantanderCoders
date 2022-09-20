'''Questão 6.
Faça uma função que recebe uma lista de números e retorna a soma dos elementos dessa lista.'''


lista = []
def soma():
    while len(lista) <= 2:
        numero = int(input("Digite um número para a lista: "))
        lista.append(numero)
    somafinal = sum(lista)
    print("A soma final da lista é", somafinal)    
        
soma()