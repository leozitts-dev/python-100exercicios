# Exercício 034 - Aumentos múltiplos
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual o salário do funcionário? \nR$'))

if salario <= 1250:
	novo = salario + (salario * 15 / 100)
else:
	novo = salario + (salario * 10 / 100)
	
print(f'O funcionário que recebia R${salario:.2f} passará a receber R${novo:.2f} após o aumento.')
