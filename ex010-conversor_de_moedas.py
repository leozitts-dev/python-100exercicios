# Exercício 010 - Conversor de Moedas
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

real = float(input('Quantos reais você tem? R$'))
cotacao = 5.64
dolar = real / cotacao
print(f'Com R${real:.2f} você consegue comprar US${dolar:.2f}')
