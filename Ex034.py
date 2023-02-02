# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Digite o salário do funcionario: '))
if sal > 1250:
    sal = sal * 0.10 + sal
    print('O novo valor do salário é {:.2f} R$ o aumento foi de 10%.'.format(sal))
else:
    sal = sal * 0.15 + sal
    print('O novo valor do salário é {:.2f} R$ o aumento foi de 15%.'.format(sal))
