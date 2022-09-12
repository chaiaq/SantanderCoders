'''Questão 3.
Crie uma função que recebe o valor do raio de um círculo como parâmetro e retorna o valor da
área desse círculo. Lembrando que a área de círculo é dada pela equação: A = ℼ r^2.
💡 Dica: Para utilizar um valor mais preciso do pi (ℼ), você pode importar a biblioteca math, e
utilizar o math.pi, como ilustrado no código abaixo:
import math
print(math.pi)'''

import math

raio = float(input("Digite o valor do raio:"))

area = (math.pi)*raio**2

print("O valor da área do círculo é:", area)