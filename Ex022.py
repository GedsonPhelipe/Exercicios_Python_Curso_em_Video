#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome = input(str('Digite o nome desejavel: ')).strip()
print('Nome em maiusculo: {}'.format(nome.upper()))
print('Nome em minusculo: {}'.format(nome.lower()))
print('Temos {} letras no nome digitado'.format(len(nome)-nome.count(' ')))
print('O primeiro nome tem {} letras'.format(nome.find(' ')))
