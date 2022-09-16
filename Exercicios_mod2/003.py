'''Faça uma função que recebe duas listas e retorna a soma item a item dessas
listas.
Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a função deve
retornar [1+3, 4+5, 3+1] = [4, 9, 4]'''

'''lista1 = []
while len(lista1) <= 2:
    numero = int(input("Digite um número para a primeira lista: "))
    lista1.append(numero)
    
lista2 = []
while len(lista2) <= 2:
    numero = int(input("Agora digite um número para a segunda lista: "))
    lista2.append(numero)'''
    
lista1=[1,2,3]
lista2=[3,2,1]
    
print(lista1, lista2)

a, b, c = lista1
print(*lista1)
d, e, f = lista2
print(*lista2)

def soma():
    soma1 = a + d
    soma2 = b + e
    soma3 = c + f
    print(soma1, soma2, soma3)
    
soma()