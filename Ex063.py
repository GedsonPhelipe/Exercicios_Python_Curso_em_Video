# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma
# Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8 

termos = int(input('Quantos termos deseja exibir: '))


matriz = 0
sequencia = 1
contador = 1


while contador <= termos:
    print(f'{matriz}', end=' -> ')
    
    resultado = matriz + sequencia    
    matriz = sequencia
    sequencia = resultado
    contador += 1
    
print('Fim')
