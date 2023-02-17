# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
# por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distan = float(input('Qual a distância da viagem? '))

if distan <= 200:
    valor = distan * 0.50
else:
    valor = distan * 0.45
print('O valor de sua viagem é {:.2f} R$'.format(valor))
