# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

vl = int(input('Digite o valor do produto: '))
print('O valor do produto com 5% de desconto é de {:.2f}'.format(vl - (vl * 5) / 100))
