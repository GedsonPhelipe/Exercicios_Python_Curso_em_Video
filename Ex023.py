# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = input('Digite um número de 0 a 9999: ')
unidade = num // 1 % 10
dezena = num // 1 % 100
centena = num // 1 % 1000
milhar = num // 1 % 10000
print()
