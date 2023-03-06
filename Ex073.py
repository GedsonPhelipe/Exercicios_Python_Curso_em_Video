# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato brasileiro de Futebol,
# na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time São Paulo.

times_brasileirao = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Internacional', 'Fluminense', 'Corinthians', 'Athletico-PR', 'Atlético', 'Fortaleza', 'São Paulo', 'América', 'Botafogo', 'Santos', 'Goiás', 'Red Bull Bragantino', 'Coritiba', 'Cuiabá', 'Grêmio', 'Vasco', 'Bahia')

print(f'Os 5 primeiros colocados do Brasileirão são {(times_brasileirao[0:5])}\n')
print(f'Os 4 últimos colocados são {(times_brasileirao[-4:])}\n')
print(f'Os times mostrados em ordem alfabética são {sorted(times_brasileirao)}\n')
print(f"O São Paulo atualmente esta na posição {times_brasileirao.index('São Paulo')+1}° posição do Brasileirão.")
