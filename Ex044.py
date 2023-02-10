# E labore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

vproduto = float(input('Digite o valor do produto: '))

print('''\nFORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque: 10% de desconto
[2] à vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço formal
[4] 3x ou mais no cartão: 20% de juros\n''')

condpag = int(input('Digite a forma de pagamento: '))

if condpag not in [1, 2, 3, 4]:
        print('Opção inválida, tente as opcões de 1 â 4.')

else:
    if condpag == 1:
        total = vproduto - (vproduto * 0.1)
        print(f'O seu desconto é de 10% e o pagamento será {total:.2f} R$.')

    elif condpag == 2:
        total = vproduto - (vproduto * 0.05)
        print(f'O seu desconto é de 5% e o pagamento será {total:.2f} R$.')

    elif condpag == 3:
        parcela = vproduto / 2
        print(f'Opção de pagamento não fornece desconto, o valor total de sua compra é {vproduto:.2f} R$.')
        print(f'O valor de sua parcela é {parcela:.2f} R$ em 2x.')

    else:
        total = vproduto + (vproduto * 0.2)
        numeroparc = int(input('Em quantas vezes deseja parcelar? '))
        parcela = total / numeroparc
        print(f'Opção de pagamento escolhida acrescenta 20% ao valor total, o novo valor de sua compra é {total:.2f} R$.')
        print(f'O valor de sua parcela é {parcela:.2f} R$ em {numeroparc}x.')
    