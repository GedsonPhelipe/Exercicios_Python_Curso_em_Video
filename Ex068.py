# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

from random import randint

vencedor = 'usuario'
resultado = ''
cont = 0

while vencedor == 'usuario':
    escolha_player = str(input('Escolha (i) para impar ou (p) para par: ' )).upper().strip()

    if escolha_player != 'I' and escolha_player != 'P':
        print('Opção inválida escolha I OU P.')
        
    else:
        player = int(input('Escolha um número de 1 à 10: '))

        if player < 1 or player > 10:
            print('Opção inválida escolha um número de 1 à 10.')
            

        else: 
            cpu = randint(1,10)
            total = player + cpu

            if total % 2 == 0:
                resultado = 'P'
            else :
                resultado = 'I'

            if escolha_player == resultado:
                vencedor ='usuario'
                cont += 1
                print('Parabéns você ganhou!')

            else:
                vencedor = 'computador'

print(f'GAME OVER, você ganhou {cont} vezes seguidas! Parábens!')
print('FIM DO PROGRAMA')
