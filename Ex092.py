#  Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
#  Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
#  Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar, considere 35 anos de contribuição independente do sexo o mesmo para aposentadoria por idade.

import datetime

aposenta = 0

dados = {'Nome': str(input('Digite o nome do trabalhador: ')).strip(),
         'CTPS': int(input('Digite o número da CTPS (Digite 0 caso não haja): '))}

ano_nasci = int(input('Digite o ano de nascimento: '))

print()

dados['Idade'] = datetime.date.today().year - ano_nasci

if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Digite o ano de contratação: '))
    dados['Salario'] = float(input('Digite o salário: '))
    dados['Aposenta'] = (dados["Contratação"] + 35) - ano_nasci
    print()

    for i, v in dados.items():
        print(f'{i} tem o valor: {v} ')

else:
    print(f'Trabalhador não possui registro em banco de dados, portanto se aposentará por idade, com 65 anos, faltam {65 - dados["Idade"]} anos.')
