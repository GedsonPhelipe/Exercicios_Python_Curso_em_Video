#  Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import randint

print('JOKENPÔ')
print('''ESCOLHA A OPÇÃO DESEJADA
[0] Para pedra
[1] Para papel
[2] Para tesoura''')

player = int(input('Qual a sua escolha? '))


if player not in [0, 1, 2]:
    print('Opção inválida,tente novamente')
else:
    cpu = randint(0,2)
    