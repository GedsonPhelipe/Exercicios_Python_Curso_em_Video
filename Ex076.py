# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ("Lápis", 1.75, "Caneta", 2.50, "Borracha", 0.50, "Caderno", 15.90,
            "Régua", 3.00, "Tesoura", 7.50, "Cola", 2.00, "Estojo", 10.00,
            "Mochila", 75.00, "Calculadora", 25.00, "Agenda", 12.50)

print("=" * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print("=" * 40)

for i in range(0, len(produtos), 2):
    print("{:.<30}R${:>7.2f}".format(produtos[i], produtos[i+1]))

print("=" * 40)
