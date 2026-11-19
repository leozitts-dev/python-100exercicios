# Exercício 026 - Primeira e última ocorrência de uma string
# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A"
# - Em que posição ela aparece a primeira vez
# - Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: \n')).strip()

print(f'A letra A aparece {frase.lower().count("a")} vezes na frase.')
print(f'A letra A aparece pela primeira vez na posição {frase.lower().find("a")+1}')
print(f'A letra A aparece pela última vez na posição {frase.lower().rfind("a")+1}')
