# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

t1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA em questão: '))

formula = t1 + (10-1) * razao
cont = 0

for c in range(t1, formula + razao, razao):
    cont = cont +1
    
    print(f'{cont}° termo é {c}')
