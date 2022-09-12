'''Questão 5.
Vamos fazer um programa para verificar quem é o assassino de um crime. Para descobrir o
assassino, a polícia faz um pequeno questionário com 5 perguntas onde a resposta só pode ser
sim ou não:
1. Mora perto da vítima?
2. Já trabalhou com a vítima?
3. Telefonou para a vítima?
4. Esteve no local do crime?
5. Devia para a vítima?
Cada resposta sim dá um ponto para o suspeito. A polícia considera que os suspeitos com 5
pontos são os assassinos, com 4 a 3 pontos são cúmplices e 2 pontos são apenas suspeitos,
necessitando de outras investigações. Valores abaixo de 2 são liberados.
No seu programa, você deve fazer essas perguntas e, de acordo com as respostas do usuário,
você vai informar como a polícia o considera.
'''


pontos = 0

print("Responda apenas com 'sim' ou 'não'")
pergunta1 = input("Mora perto da vítima? ")
if pergunta1 == 'sim':
    pontos = pontos + 1
    
pergunta2 = input("Já trabalhou com a vítima? ")
if pergunta2 == 'sim':
    pontos = pontos + 1
    
pergunta3 = input("Telefonou para a vítima? ")
if pergunta3 == 'sim':
    pontos = pontos + 1
    
pergunta4 = input("Esteve no local do crime? ")
if pergunta4 == 'sim':
    pontos = pontos + 1
    
pergunta5 = input("Devia para a vítima? ")
if pergunta5 == 'sim':
    pontos = pontos + 1
    
pontos = int(pontos)

if pontos == 5:
    print("Assassino!")
elif pontos >= 3:
    print("Cúmplice!")
elif pontos == 2:
    print("Suspeito!")
else:
    print("Liberado!")