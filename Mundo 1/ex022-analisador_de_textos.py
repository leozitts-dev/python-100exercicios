# Exercício 022 - Analisador de Textos
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas
# - Quantas letras ao todo (sem considerar espaços)
# - Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
separado = nome.split()

print(f'Analisando seu nome...')
print(f'Seu nome em MAIÚSCULAS é: {nome.upper()}')
print(f'Seu nome em minúsculas é: {nome.lower()}')
print(f'Seu nome tem {len(nome)-nome.count(' ')} letras.')
print(f'Seu primeiro nome é {separado[0]} e ele tem {len(separado[0])} letras.')
