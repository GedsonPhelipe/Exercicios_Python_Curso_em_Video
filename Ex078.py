#  Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#  No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []

for i in range(5):
    valor = int(input(f'Digite o {i}º valor: '))
    valores.append(valor)

maior_valor = max(valores)
menor_valor = min(valores)

ocorrencias_maior_valor = []
ocorrencias_menor_valor = []

for i, valor in enumerate(valores):
    if valor == maior_valor:
        ocorrencias_maior_valor.append(i)

    elif valor == menor_valor:
        ocorrencias_menor_valor.append(i)

print(f'O maior valor digitado foi {maior_valor} nas posições {ocorrencias_maior_valor}')
print(f'O menor valor digitado foi {menor_valor} nas posições {ocorrencias_menor_valor}')
