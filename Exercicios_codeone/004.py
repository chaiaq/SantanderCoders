'''Questão 4.
Faça um programa que peça 2 números inteiros e um número real, calcule e mostre:
a) o produto entre o dobro do primeiro e a metade do segundo.
b) a soma entre o triplo do primeiro e o terceiro.
c) o terceiro elevado ao cubo.'''

int1 = int(input("Digite um número inteiro:"))

int2 = int(input("Digite outro número inteiro:"))

real = float(input("Digite um número real:"))

a = (int1*2)*(int2/2)
b = (int1*3)+(real)
c = real**3

print("O resultado de A é", a)
print("O resultado de B é", b)
print("O resultado de C é", c)