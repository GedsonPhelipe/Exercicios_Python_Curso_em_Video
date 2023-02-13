#  Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import randint

print('JOKENPÔ!!!\n')
print('''ESCOLHA A OPÇÃO DESEJADA
[0] Para pedra
[1] Para papel
[2] Para tesoura''')

player = int(input('\nQual a sua escolha? '))

if player not in [0, 1, 2]:
    print('Opção inválida,tente novamente de 0 à 2')

else:
    itens = ['pedra', 'papel','tesoura']
    cpu = randint(0,2)

    print('JO!')
    sleep(1/2)
    print('KEN!')
    sleep(1/2)
    print('PÔ!')

    if player == cpu:
        print(f'O computador também escolheu {itens[cpu]} então EMPATE!')

    elif (cpu == 0 and player == 1) or (cpu == 1 and player == 2) or (cpu == 2 and player == 0):
        print(f"O computador escolheu {itens[cpu]}, PARABÉNS VOCÊ VENCEU!")
    
    else:
        print(f'O computador escolheu {itens[cpu]}, sinto muito você perdeu, tente novamente! ')
