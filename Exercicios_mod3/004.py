'''4 - Você conhece Star Wars? Se trata, obviamente, da famosa saga espacial
criada por George Lucas em 1977 e que deu origem a símbolos do cinema e
da cultura pop com o imponente vilão Darth Vader ou o simpático robô
R2-D2. A ideia desse exercício é justamente extrair informações do
personagem Darth Vader através de uma API de Star Wars chamada SWAPI.
Utilize a URL "https://swapi.dev/api/people/4/" para fazer a requisição dos
dados de Darth Vader e extraia as informações "name" (nome), "height"
(altura), "mass" (massa) e "birth_year" (ano de nascimento) e imprima cada
dado em uma linha.'''

import requests
url = 'https://swapi.dev/api/people/4/'
requisicao = requests.get(url)
dados = requisicao.json()
print(dados)

print(dados['name'])
print(dados['height'])
print(dados['mass'])
print(dados['birth_year'])