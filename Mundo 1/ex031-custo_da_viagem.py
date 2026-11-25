# Exercício 031 - Custo da Viagem
# Desenvolva um programa que pergunte a distância de uma viagem em km e calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.

distancia = float(input('Qual a distância da viagem? (km) \n'))
custo1 = distancia * 0.50
custo2 = distancia * 0.45

if distancia > 200:
	print(f'O valor a pagar pela viagem é de R${custo2:.2f}')
else:
	print(f'O valor a pagar pela viagem é de R${custo1:.2f}')
