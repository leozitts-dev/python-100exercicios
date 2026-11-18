# Exercício 018 - Seno, Cosseno e Tangente
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
angulo = float(input('Digite o ângulo: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print(f'O ângulo de {angulo}⁰ tem o SENO de {sen:.2f}')
print(f'O ângulo de {angulo}⁰ tem o COSSENO de {cos:.2f}')
print(f'O ângulo de {angulo}⁰ tem a TANGENTE de {tan:.2f}')
