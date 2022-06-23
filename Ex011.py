# Faça um programa que leia a largura e a altura de uma parede em metros,calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

alt = int(input('Digite a altura da parede em metros: '))
larg = int(input('Digite a largua da parede em metros: '))
area = alt*larg
tint = area/2
print('A area da parede em questão é {} m², serão necessarios {} litros para uma cobertura total'.format(area, tint))
