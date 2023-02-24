# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

contador = 0
soma = 0
num = 0

while num != 999:
    num = int(input('Digite o número desejado, caso deseje parar digite 999: '))
    if num != 999:
        contador += 1
        soma += num

print(f'Você digitou {contador} números e a soma entre eles é {soma}.') 
