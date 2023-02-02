# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o teceiro número: '))
# Teste maior
maior = 1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > 2 and num3 > num1:
    maior = num3
# Teste menor
menor = 1
if num2 < num1 and num2 < num3:
    maior = num2
if num3 < 2 and num3 < num1:
    maior = num3
print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))
