'''Questão 2.
Crie um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual
dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Caso o valor não
esteja em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”. Veja
alguns exemplo abaixo:
💡 Entrada: 25.01 | Saída: (25,50]
Entrada: 25.00 | Saída: [0,25]
Entrada: 100.00 | Saída: (75,100]
Entrada: -25.02 | Saída: Fora de intervalo'''





valor = int(input('Digite um número:'))
if valor <= 25:
    print(valor, "está no intervalo [0,25]")
elif valor <= 50:
    print(valor, "está no intervalo (25,50]")
elif valor <= 75:
    print(valor, "está no intervalo (50,75]")
elif valor <= 100:
    print(valor, "está no intervalo (75,100]")
else:
    print("Fora de intervalo")