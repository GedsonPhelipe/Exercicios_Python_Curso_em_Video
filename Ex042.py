#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes 

r1 = float(input('Digite o valor do primeiro seguimento: '))
r2 = float(input('Digite o valor do segundo seguimento: '))
r3 = float(input('Digite o valor do terceiro seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triângulo!')
    if r1 == r2 == r3:
        print('O triângulo formado é EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print('O triângulo formado é ESCALENO.')
    else:
        print('O triÂngulo formado é ISÓSCELES')
else:
    print('Os seguimentos acima não podem formar um triângulo!')
    