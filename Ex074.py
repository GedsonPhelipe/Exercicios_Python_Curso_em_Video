# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
# mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

import random

numeros = tuple(sorted(random.sample(range(1, 100), 5)))

print(numeros)
print(f'O maior número listado é {(numeros[4])} e o menor é {(numeros[0])}')
# ou print(f'O maior número listado é {max(numeros)} e o menor é {min(numeros)}')
