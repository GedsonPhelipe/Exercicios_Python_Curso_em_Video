# Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. 

opcao = 0

while opcao != 5:
    valor1 = float(input('Digite o primeiro valor da operação: '))
    valor2 = float(input('Digite o segundo valor da operação: '))

    print('\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')

    opcao = int(input('\nDigite o operação desejada: '))

    if opcao == 1:
        soma = valor1 + valor2
        print(f'A soma dos valores {valor1} e {valor2} é {soma}\n')

    elif opcao == 2:
        multiplica = valor1 * valor2
        print(f'O resultado da multiplicação entre {valor1} e {valor2} é {multiplica}\n')

    elif opcao == 3:
        if valor1 > valor2:
            print(f'O maior valor digitado foi {valor1}\n')
        else: 
            print(f'O maior valor digitado foi {valor2}\n')

    elif opcao == 4:
        print('Você escolheu a opção para novos valores, por favor digite novamente os dois valores desejados!\n')

print('Fim do programa')
