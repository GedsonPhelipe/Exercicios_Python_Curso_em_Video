# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0

for c in range(1, 7):
    termo = int(input('Digite o termo: '))

    if termo % 2 == 0:
            soma = soma + termo
            
            cont = cont + 1
            
print(f'Você digitou {cont} termos pares e soma dos valores pares digitados é {soma}.')
