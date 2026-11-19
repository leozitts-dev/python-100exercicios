# Exercício 025 - Procurando uma string dentro de outra
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Qual o seu nome completo? \n'))
print(f'Seu nome tem Silva? {"silva" in nome.lower()}')
