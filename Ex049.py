# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

tab = int(input('Digite o número da tabuada que deseja: '))

if tab <= 0:
    print('Número de taboada inválido tente um valor de 1 à 10.')
    
else:
    print(f'TABOADA DO {tab}\n')

    for cont in range(1, 11):
        mult = cont * tab

        print(f'{tab} x {cont} = {mult}')
