# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

from datetime import date

ano = int(input('Digite o ano de nascimento do atleta: '))

if ano <= 0:
    print('*ERRO: O ANO DE NASCIMENTO DEVE SER MAIOR QUE 0.')
else:
    idad = date.today().year - ano
    categ = ''

    if idad <0:
        categ = '*ERRO: O ANO DE NASCIMENTO DIGITADO É SUPERIOR AO ANO ATUAL.'
    elif idad <= 9:
        categ = 'MIRIM'
    elif idad <= 14:
        categ = 'INFANTIL'
    elif idad <= 19:
        categ = 'JÚNIOR'
    elif idad <= 25:
        categ = 'SÊNIOR'
    else:
        categ = 'MASTER'

    print(f'O atleta tem {idad} anos.')
    print(f'A categoria do atleta é {categ}')
