#  Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
#  conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
#  listas geradas.

resposta = 'S'
lista = []
pares = []
impares = []

while resposta == 'S':
    valor = (int(input('Digite o valor desejado para a lista: ')))
    lista.append(valor)

    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

    while True:
        resposta = input('Deseja continuar digitando? (S/N): ').strip().upper()
        if resposta in 'SN':
            break
        else:
            print('Resposta inválida digite S ou N.')


print(f'Os valores atribuídos a lista foram {lista}')
print(f'Os valores pares são: {pares}')
print(f'Os valores ímpares são: {impares}')
