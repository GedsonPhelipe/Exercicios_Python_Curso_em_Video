# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idade = 0
mais_velho = 0
nome_maisvelho = ""
contador_mulher20 = 0

for test in range(1, 5):
    nome = str(input(f'Digite o nome da {test}° pessoa: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    soma_idade = soma_idade + idade

    if sexo == 'M' and idade > mais_velho:
        mais_velho = idade
        nome_maisvelho = nome

    if sexo == 'F' and idade < 20:
        contador_mulher20 = contador_mulher20 + 1

media = soma_idade / 4

print(f'A média de idade dos participantes é {media:.1f}')
print(f'O homem mais velho se chama {nome_maisvelho}')
print(f'Das mulheres analisadas, {contador_mulher20} tem menos de 20 anos.')
