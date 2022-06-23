# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e
# mostre o comprimento da hipotenusa.

import math
catop = float(input('Digite o comprimento do cateto oposto:'))
catad = float(input('Digite o comprimento do cateto adjascente: '))
hi = math.hypot(catop, catad)
print('O valor da hipotenusa é {:.2f}!'.format(hi))
