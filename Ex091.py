# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogos = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6), 'jogador 3': randint(1, 6), 'Jogador 4': randint(1, 6)}

for j, d in jogos.items():
    print(f'O {j} tirou o número {d}.')
    sleep(1/2)

ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)

print()
print('-*-'*11)
print('   == RANKING DE JOGADORES ==')
print()
for i, v in enumerate(ranking):
    print(f'  {i+1}º colocado: {v[0]} tirou {v[1]}')
print('-*-'*11)
