# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

maiores18 = 0
homens = 0
mulheres_menos20 = 0
resposta = 'S'

while resposta == 'S':
    idade = int(input('Digite a idade: '))
    
    if idade <= 0:
        print('Idade inválida digite um NÚMERO acima de 0.\n')
    else:
        while True:
            sexo = str(input('Digite o sexo (M/F): ')).strip().upper()

            if sexo != 'M' and sexo != 'F':
                print('Sexo inválido digite M OU F,\n')
            else:
                resposta = str(input('Deseja continuar (S/N): ')).strip().upper()
                
                if idade > 18:
                    maiores18 += 1

                if sexo == 'M':
                    homens += 1
                else: 
                    if idade < 20:
                        mulheres_menos20 += 1
                break

print(f'{maiores18} pessoas tem mais de 18 anos, {homens} homens foram analisdaos, {mulheres_menos20} mulheres tem menos de 20 anos.')
