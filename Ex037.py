# Escreva um programa em Python que leia um número inteiro qualquer 
# e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. 

num = int(input('Digite o número para conversão: '))

print('\n1 para binário')
print('2 para octal')
print('3 para hexadecimal\n')

op = int(input('Digite a opção desejeada: '))

if op == 1:
    print('o número {} em binário é {}.'.format(num, bin(num)[2:]))
elif op == 2:
    print('o número {} em octal é {}.'.format(num,oct(num)[2:]))
elif op == 3:
    print('o número {} em hexadecimal é {}.'.format(num,hex(num)[2:]))
else:
    print('Opção inválida, tente novamente.')
