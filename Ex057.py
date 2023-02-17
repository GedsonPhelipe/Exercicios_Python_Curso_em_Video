# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado,
#  peça a digitação novamente até ter um valor correto.

opcoes = ['M', 'F', 'MASCULINO', 'FEMININO']

sexo = str(input('Digite o sexo, (M/F):'  )).strip().upper()

while sexo not in opcoes:
    sexo = str(input('Sexo digitado inválido, por favor digite o sexo, (M/F):'  )).strip().upper()

print(f'Sexo {sexo} registrado com sucesso.')
