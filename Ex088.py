# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random

lista_jogos = []
num_jogos = int(input('Quantos jogos quer que eu sorteie? '))

for c in range(num_jogos):
    jogo = random.sample(range(1, 61), 6)
    jogo.sort()
    lista_jogos.append(jogo)
    print(f'Jogo {c + 1}: {jogo}')
