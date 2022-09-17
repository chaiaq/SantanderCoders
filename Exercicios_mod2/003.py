'''Faça uma função que recebe duas listas e retorna a soma item a item dessas
listas.
Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a função deve
retornar [1+3, 4+5, 3+1] = [4, 9, 4]'''

lista1 = []
while len(lista1) <= 2:
    numero = int(input("Digite um número para a primeira lista: "))
    lista1.append(numero)
    
lista2 = []
while len(lista2) <= 2:
    numero = int(input("Agora digite um número para a segunda lista: "))
    lista2.append(numero)
    
def soma ():
    for numero in zip(lista1, lista2):
        print(sum(numero))

soma()