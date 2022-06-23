# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

cel = float(input('Digite o valor da temperatura em °C: '))
fahr = (9*cel)/5+32
print('A temperatura convertida para Fahreinheit é: {} °F'.format(fahr))
