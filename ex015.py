# Exercício 015 - Aluguel de Carros
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Por quantos dias o carro foi alugado? \n'))
km = float(input('Quantos Quilômetros foram rodados? \n'))
pago = (dias * 60) + (km * 0.15)

print(f'O total a pagar pelo aluguel do carro é: \nR${pago:.2f}')
