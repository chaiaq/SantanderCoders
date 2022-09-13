'''Faça um programa que peça um valor monetário e diminua-o em 15%.
Seu programa deve imprimir a mensagem “O novo valor é [valor]”.'''

valor = input("Digite o valor do produto: ")
desconto = float(valor) * 0.15
novovalor = float(valor) - desconto
print("O novo valor é", novovalor)