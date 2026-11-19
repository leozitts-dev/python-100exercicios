# Exercício 023 - Separando dígitos de um número
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Exemplo: unidade, dezena, centena e milhar

num = int(input('Digite um valor entre 0 e 9999:\n'))

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print(f'Analisando o número {num}')
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
