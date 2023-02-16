# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não   # atingiram a maioridade e quantas já são maiores.

from datetime import date

menores = 0
maiores = 0
analisados = 0
invalidos = 0

for c in range(7):
    ano_nasc = int(input('Digite o ano de nascimento: '))

    if ano_nasc <= 0 or ano_nasc > date.today().year:
        print('Ano inválido! O ano digitado não pode ser maior que o ano atual, ou menor que 0.')

        invalidos = invalidos + 1

    else:
        idade = date.today().year - ano_nasc

        analisados = analisados + 1
        
        if idade < 18:
            menores = menores + 1
            
        else:
            maiores = maiores + 1

print(f'Dos {analisados} indivíduos analisados {maiores} são maiores, e {menores} são menores.')
print(f'{invalidos} indivíduos não puderam ser avaliados.')
