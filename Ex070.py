# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

resposta = "S"
mais_caro = ''
nome_mais_barato = ""
mais_barato = 0
mais_1000 = 0
total = 0

while resposta == "S":
    nome_produto = str(input('Digite o nome do produto em questão: '))
    preco = float(input('Digite o preço do produto: '))
    
    while True:
        resposta = str(input('Deseja continuar? (S/N): ')).strip().upper()
        
        if resposta != 'S' and resposta != "N":
            print('Resposta inválida por favor digite S OU N.')
        else:
            total += preco
            if preco > 1000:
                mais_1000 += 1

            if mais_barato == 0:
                mais_barato = preco
                nome_mais_barato = nome_produto
            else:
                if preco < mais_barato:
                    mais_barato = preco
                    nome_mais_barato = nome_produto
                    
            break

print(f'O total da compra é de {total:.2f} R$.')
print(f'{mais_1000} produtos custão mais que 1000.00 R$')
print(f'o produto mais barato foi {nome_mais_barato}, custando {mais_barato:.2f} R$.')
