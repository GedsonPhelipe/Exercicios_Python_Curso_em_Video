# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o
# jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

print('Vou pensar em um número de 0 à 10, você consegue acerta-lo?')

computador = randint(0,10)
tentativas = 1

print('Pensando...')
sleep(3)

usuario = int(input('Digite o seu palpite: '))

while usuario != computador:
    usuario = int(input('Você errou tente novamente:  '))
    tentativas = tentativas +1

print(f'Parábens você acertou! Foram necessarías {tentativas} tentativas até o acerto.')
