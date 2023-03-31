# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expres = str(input('Digite a expressão desejada: '))
verif = []
for simb in expres:
    if simb == '(':
        verif.append('(')
    elif simb == ')':
        if len(verif) > 0:
            verif.pop()
        else:
            verif.append(')')
if len(verif) == 0:
    print('Sua expressão está válida.')
else:
    print('Sua expressão não é válida.')
