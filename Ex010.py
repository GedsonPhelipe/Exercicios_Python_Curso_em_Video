# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

v = int(input('Quantos reais o usuario possui?: '))
conver = v / 5.15
print('O usuario pode comprar {:.2f} Dollares'.format(conver))
