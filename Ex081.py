# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

resposta = 'S'
lista = []

while resposta == 'S':
    lista.append(int(input('Digite o valor desejado: ')))

    while True:
        resposta = str(input('Deseja continuar digitando? (S/N): ')).strip().upper()
        if resposta in 'SN':
            break
        else:
            print('Resposta inválida, digite S ou N.')

if 5 in lista:
    print(f'O número 5 foi digitado {lista.count(5)} vezes')
else:
    print('O número 5 não foi digitado na lista em questão. ')

print(f'Foram atribuidos {len(lista)} valores para a lista.')
print(f'A lista de valores digitados em ordem decrescente é {sorted(lista, reverse=True)}')
