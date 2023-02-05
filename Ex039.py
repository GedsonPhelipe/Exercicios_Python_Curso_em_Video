# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar
# ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.Seu programa também deverá
# mostrar o tempo que falta ou que passou do prazo.

from datetime import date

nasc = int(input('Digite o ano de seu nascimento: '))
idade = date.today().year - nasc

if idade < 18:
    falt = 18 - idade
    print('Faltam {} anos para se alistar.'.format(falt))
elif idade == 18:
    print('Esse é o ano para se alistar não se esqueça!')
else:
    atraso = idade - 18
    print('Você está atrasado {} anos, procure urgentemente a junta militar de seu munícipio!'.format(atraso))
