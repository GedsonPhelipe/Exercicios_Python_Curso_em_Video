# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

items = ('arroz', 'colher', 'sal', 'cadeira', 'microondas')
vogais = ()

for palavras in items:
    for letra in palavras:
        if letra in 'aeiou':
            vogais += (letra,)
    print(f'Na palavra {palavras} contém as vogais{vogais}')
    vogais = ()
