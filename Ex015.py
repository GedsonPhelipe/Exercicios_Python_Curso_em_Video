# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos KM s foram percorridos com o veiculo: '))
dias = float(input('Por quantos dias o veiculo foi alugado: '))
vpago = (km*0.15)+(dias*60)
print('O valor a ser pago é de {:.2f} R$'.format(vpago))
