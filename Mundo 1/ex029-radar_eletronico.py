# Exercício 029 - Radar eletrônico
# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual a velocidade atual do carro em km/h? \n'))
multa = (velocidade-80) * 7

if velocidade > 80:
	print(f'MULTADO! Você excedeu o limite de velocidade que é 80km/h \nTotal a pagar: R${multa:.2f}')
else:
	print('Tenha um bom dia! Dirija com cuidado.')
