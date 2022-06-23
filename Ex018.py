# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
ang = int(input('Digite o ângulo desejado: '))
angc = radians(ang)
print('Referente ao ângulo de {} graus os resultados são:'.format(ang))
print('seno: {:.2f}\ncosseno: {:.2f}\ntangente: {:.2f}'.format(sin(angc), cos(angc), tan(angc)))
