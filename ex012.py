# Exercício 012 - Calculando Descontos
# Faça um algoritmo que leia o preço e o valor do desconto de um produto e mostre seu novo preço com o desconto.

valor = float(input('Digite o valor do produto: R$'))
desconto = float(input('Quanto de desconto esse produto tem? %'))
valor_desconto = float((valor * desconto) / 100)
valor_final = float(valor - valor_desconto)
print(f'O produto que antes custava R${valor:.2f} com um desconto de {desconto:.0f}% terá o valor de R${valor_final:.2f}')
print(f'Você economizará R${valor_desconto:.2f}')
