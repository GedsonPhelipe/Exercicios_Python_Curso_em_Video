# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. 

# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


total = 0
cedula_atual = 50
total_cedula = 0

valor = int(input('Digite o valor desejado para o saque: '))
total = valor

if valor <= 0:
    print('Valor inválido o valor de saque deve ser maior que 0')
else:
    while True:
        if total >= cedula_atual:
            total -= cedula_atual
            total_cedula += 1
        else:
            if total_cedula > 0:
                print(f'Foram {total_cedula} cédulas de {cedula_atual} R$.')
            
            if cedula_atual == 50:
                cedula_atual = 20
                total_cedula = 0

            elif cedula_atual == 20:
                cedula_atual = 10
                total_cedula = 0
                
            elif cedula_atual == 10:
                cedula_atual = 1
                total_cedula = 0

            if total == 0:
                break
