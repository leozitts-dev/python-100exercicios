# Exercício 011 - Pintando Parede
# Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

altura_cm = float(input('Qual a altura da parede em centímetros? \n'))
largura_cm = float(input('Qual a largura da parede em centímetros? \n'))
altura = altura_cm / 100
largura = largura_cm / 100
area = altura * largura
tinta = area / 2

print(f'A parede tem a dimensão de {altura_cm}x{largura_cm}')
print(f'A área da parede é {area:.2f}m²')
print(f'Você vai precisar de {tinta:.2f} litros de tinta para pinta-la.')
