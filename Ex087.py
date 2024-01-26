# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = 0
somaterc = 0
valoressecundl = []

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

for l in range(0, 3):
    for c in range(0, 3):
        (print(f'[{matriz[l][c]:^5}]', end=''))

        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]

        if c == 2:
            somaterc += matriz[l][c]

        if l == 1:
            valoressecundl.append(matriz[l][c])

    print()
print(f'A soma dos valores pares é: {somapares}')
print(f'A soma dos valores da terceira coluna é: {somaterc}')
print(f'O valor mais alto digitado na segunda linha é: {max(valoressecundl)}')
