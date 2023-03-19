# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

valores_usuario = []

for c in range(5):
    valor = int(input('Digite o valor desejado: '))

    if c == 0 or valor > valores_usuario[-1]:
        valores_usuario.append(valor)

    else:
        pos = 0
        while pos < len(valores_usuario):
            if valor <= valores_usuario[pos]:
                valores_usuario.insert(pos, valor)
                break
            pos += 1
print(f'Os valores digitados em ordem foram {valores_usuario}')
