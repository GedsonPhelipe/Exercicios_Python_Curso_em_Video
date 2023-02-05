# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorim = float(input('Digite o valor do imóvel: '))
renda = float(input('Digite o valor da renda do comprador: '))
prazo = int(input('Em quantos anos será o pagamento? '))

parcela = valorim / (prazo * 12) 
cond = renda * 0.3

print('Para realizar o financiamento de um imóvel no valor de {:.2f} o valor da parcela é de {:.2f} R$, em {} anos'.format(valorim,parcela,prazo))

if parcela > cond:
    print('Sentimos muito seu fincanciamento não foi aprovado.')
else:
    print('Parabéns seu fincanciamento foi aprovado!')
    