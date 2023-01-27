#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input("Digite o nome da cidade em que nasceu: ")).strip().upper()
if cidade[0:5] == "SANTO":
    print('Sua cidade começa com a palavra "Santo"')
else:
    print('Sua cidade não começa com a palavra "Santo"')