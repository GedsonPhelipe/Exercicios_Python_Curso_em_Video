# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

valores = ()
pares = ()

for c in range(1, 5):
    usuario = int(input(f'Digite o {c} valor: '))
    valores += (usuario,)

    if usuario % 2 == 0:
        pares += (usuario,)
    
if 9 in valores:
    print(f'O valor 9 foi digitado {valores.count(9)} vezes ')
else:
    print('O valor 9 não foi digitado nenhuma vez.')

if 3 in valores:
    print(f'O primeiro 3 foi digitado na posição {valores.index(3)+1}')
else:
    print('O valor 3 não foi digitado nenhuma vez.')

print(f'Os valores pares digitados são {pares}')
