# Exercício 013 - Reajuste Salarial
# Faça um algoritmo que leia o salário de um funcionário e quanto de aumento ele teve e então mostre seu novo salário.

salario = float(input('Qual o salário do funcionário? \n R$'))
aumento = int(input('Qual o valor do aumento? \n %'))
novo_salario = salario + (salario * aumento / 100)

print(f'Um funcionário que antes tinha o salário de R${salario:.2f} com um aumento de {aumento:.0f}% passará a receber um salário de R${novo_salario:.2f}.')
