# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

contador = 0
acumulador = 0
maior = 0
menor = 0
resposta = 'S'

while resposta in 'S':
    num = int(input('Digite o número desejado: '))
    acumulador += num
    contador += 1

    if contador == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resposta = str(input('Deseja continuar digitando, digite S para continuar ou N para finalizar: ')).strip().upper()

media = acumulador / contador
print(f'\nVocê digitou {contador} termos.')
print(f'\nO maior número digitado foi {maior}, o menor foi {menor} e a media de todos os números digitados é {media}.')
print('\nFim do programa.')
