# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input("Qual seu nome completo? ")).strip().upper()
if 'SILVA' in nome:
    print('Seu nome contém a palavra "Silva"')
else:
    print('Seu nome não contém a palavra "Silva"')
