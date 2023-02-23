# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa
# encerrará quando ele disser que quer mostrar 0 termos

t1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA em questão: '))

cont = 1
acumulador = t1
mais = 10
total = 0

while mais != 0:
    total += mais

    while cont <= total:
        print(f'{acumulador} -> ', end ='')

        cont += 1
        acumulador += razao

    print('Pausa')
    mais = int(input('Quantos termos mais deseja ver? '))
    
print('Fim')
