# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela. Média igual ou maior que 7 passa.

aluno = dict()

aluno['Nome'] = str(input('Digite o nome do aluno: '))
aluno['Media'] = float(input(f'Digite a média de {aluno["Nome"]}: '))

if aluno['Media'] >= 7:
    aluno['Situacao'] = 'APROVADO'

elif 5 <= aluno['Media'] < 7:
    aluno['Situacao'] = 'RECUPERAÇÃO'

else:
    aluno['Situacao'] = 'REPROVADO'

print(f'O aluno {aluno["Nome"]} com média {aluno["Media"]} ficou com status de: {aluno["Situacao"]}.')
