# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida 

peso = float(input('Digite o peso em (KG):  '))
alt = float(input('Digite a altura: '))

if peso <= 0 or alt <=0:
    print('Os valores informados não podem ser inferiores ou igual a 0.')
else:
    imc = peso / (alt * alt)
    if imc < 18.5:
        print(f'O IMC é {imc:.1f}, o paciente está ABAIXO do peso ideal.')
    elif imc >= 18.5 and imc <= 25:
        print(f'O IMC é {imc:.1f}, o paciente está no peso ideal!')
    elif imc >= 25 and imc <= 30:
        print(f'O IMC é {imc:.1f}, o paciente está com sobrepeso')
    elif imc >= 30 and imc <= 40:
        print(f'O IMC é {imc:.1f}, o paciente está com obesidade !')
    else:
        print(f'O IMC é {imc:.1f}, e o paciente está com obesidade mórbida!')
