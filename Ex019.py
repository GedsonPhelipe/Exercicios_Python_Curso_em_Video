# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random
alun1 = input('Digite o nome do primeiro aluno: ')
alun2 = input('Digite o nome do segundo aluno: ')
alun3 = input('Digite o nome do terceiro aluno: ')
alun4 = input('Digite o nome do quarto aluno: ')
lista = [alun1, alun2, alun3, alun4]
print('O aluno escolhido foi: {}'.format(random.choice(lista)))
