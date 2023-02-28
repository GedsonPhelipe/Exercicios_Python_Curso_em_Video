# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

cont = 0

from time import sleep

while True:
    tab = int(input('\nDigite a tabuada desejada, para encerrar digite um número negativo: '))
    if tab > 0: 
        while cont <10:
            cont += 1
            resultado = tab * cont
            print(f'{tab} x {cont} = {resultado}')
            sleep(0.5)
        cont = 0
    
    else:
        print('PROGRAMA DE TABUADA ENCERRADO.Volte sempre!')
        break
