#  Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#  A) Quantas pessoas foram cadastradas.
#  B) Uma listagem com as pessoas mais pesadas.
#  C) Uma listagem com as pessoas mais leves.

principal = []
temp = []
resposta = 'S'
mais_pesado = []
mais_leve = []

while resposta == 'S':
    temp.append(str(input('Digite o nome do paciente: ')))
    temp.append(float(input('Digite o peso do paciente: ')))

    if len(principal) == 0:
        mais_pesado = mais_leve = temp[1]
    else:
        if temp[1] > mais_pesado:
            mais_pesado = temp[1]
        if temp[1] < mais_leve:
            mais_leve = temp[1]

    principal.append(temp[:])
    temp.clear()

    while True:
        resposta = str(input('Deseja continuar digitando? Digite S/N: ')).upper().strip()
        if resposta in 'SN':
            break
        else:
            print('Resposta inválida digite S ou N.')


print(f'Foram cadastradas {len(principal)} pessoas.')

print(f' Maior peso: {mais_pesado} KG. Peso de ', end='')
for p in principal:
    if p[1] == mais_pesado:
        print(f'[{p[0]}]', end='')
print()

print(f' Menor peso: {mais_leve} KG. Peso de ',end='')
for p in principal:
    if p[1] == mais_leve:
        print(f'[{p[0]}]', end='')
