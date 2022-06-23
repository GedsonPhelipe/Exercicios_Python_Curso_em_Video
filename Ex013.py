# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

fun = str(input('Digite o nome do funcionario: '))
sal = int(input('Digite o salario atual do funcionario:'))
nsal = sal + (sal * 5 / 100)
print('O novo salario do funcionario {} será {:.2f} R$'.format(fun, nsal))
