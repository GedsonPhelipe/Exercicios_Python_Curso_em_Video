# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

frase = input('Digite a frase a ser analisada: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[: : -1]

if inverso == junto:
    print(f'A frase digitada é um palíndromo!')
    
else:
    print('A frase digitada NÃO é um palíndromo.')
