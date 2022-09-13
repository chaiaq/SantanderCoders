'''Faça um programa que leia a validade das informações:
a. Idade: entre 0 e 150;
b. Salário: maior que 0;
c. Sexo: M, F ou Outro;

O programa deve imprimir uma mensagem de erro para cada informação inválida.'''

idade = int(input('Digite a idade (entre 0 e 150 anos): '))
if idade < 0 or idade > 150:
    print('Por favor, digite uma idade entre 0 e 150 anos')

salario = float(input('Digite seu salário: '))
if salario <= 0:
    print('Por favor, digite um salário maior que R$ 0,00')

sexo = str(input("Digite o sexo: F, M ou Outro: "))
if sexo != 'F' and sexo != 'M' and sexo != 'Outro':
    print('Por favor, digite apenas "F", "M" ou "Outro"')