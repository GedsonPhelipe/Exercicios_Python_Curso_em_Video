# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que
# leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

alun1 = input('Digite o nome do primeiro aluno: ')
alun2 = input('Digite o nome do segundo aluno: ')
alun3 = input('Digite o nome do terceiro aluno: ')
alun4 = input('Digite o nome do quarto aluno: ')
lista = [alun1, alun2, alun3, alun4]
random.shuffle(lista)
print('A ordem de apresentação sorteada foi: {}'.format(lista))
