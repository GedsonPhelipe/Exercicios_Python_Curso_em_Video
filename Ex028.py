# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu
# ou perdeu.

from random import randint
from time import sleep
print('Vou pensar em um número de 0 à 5, você consegue acerta-lo?')
computador = randint(0,5)
usuario = int(input('Digite o seu palpite: '))
print('Pensando...')
sleep(3)
if computador == usuario:
    print('PARABÉNS VOCÊ ACERTOU!')
else:
    print('VOCÊ ERROU TENTE DE NOVO!')
