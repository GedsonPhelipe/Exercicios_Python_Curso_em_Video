# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Digite o valor do primeiro seguimento: '))
r2 = float(input('Digite o valor do segundo seguimento: '))
r3 = float(input('Digite o valor do terceiro seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triângulo!')
else:
    print('Os seguimentos acima não podem formar um triângulo!')
    