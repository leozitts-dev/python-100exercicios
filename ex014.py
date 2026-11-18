# Exercício 014 - Conversor de Temperaturas
# Escreva um programa que converta uma temperatura digitada em ºC para ºF.

C = float(input('Digite a temperatura em ⁰C \n'))
F = C * 1.8 + 32

print(f'{C:.0f}⁰C equivale a {F}⁰F')
