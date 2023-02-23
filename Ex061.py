# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10
# primeiros termos da progressão usando a estrutura while.


t1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA em questão: '))

cont = 1
acumulador = t1

while cont <= 10:
    print(f'{acumulador} -> ', end ='')
    
    cont += 1
    acumulador += razao

print('Fim')
