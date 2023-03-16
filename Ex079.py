# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados
# em ordem crescente.

resposta = 'S'
valores_usuario = []

while resposta == 'S':
    valor = int(input('Digite o valor: '))

    if valor not in valores_usuario:
        valores_usuario.append(valor)
    else:
        print('Valor ja registrado anteriormente,digite um valor diferente.')
    while True:
        resposta = input('Deseja continuar? (S/N): ').strip().upper()
        if resposta in 'SN':
            break
        else:
            print('Resposta inválida digite S para continuar ou N para parar.')

print(f'Os valores digitados foram {sorted(valores_usuario)}')
