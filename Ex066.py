# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag). (NOVAMENTE, DESSA VEZ USANDO 'BREAK')

contador = 0
soma = 0
num = 0

while True:
    num = int(input('Digite o número desejado, caso deseje parar digite 999: '))
    if num != 999:
        contador += 1
        soma += num
    else:
        break

print(f'Você digitou {contador} números e a soma entre eles é {soma}.') 
