# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

v = float(input('Digite um valor em metros: '))
print('O valor em centrimetros é {}cm, e em milimetros é {}mm'.format(v*100, v*1000))
