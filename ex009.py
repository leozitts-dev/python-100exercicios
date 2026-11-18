# Exercício 009 - Tabuada
# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Digite um número para ver sua tabuada: '))

t1 = n * 1
t2 = n * 2
t3 = n * 3
t4 = n * 4
t5 = n * 5
t6 = n * 6
t7 = n * 7
t8 = n * 8
t9 = n * 9
t10 = n * 10

print('-' * 20)
print(f'A tabuada de {n} é:')
print(f'{n} x {1:2} = {t1}')
print(f'{n} x {2:2} = {t2}')
print(f'{n} x {3:2} = {t3}')
print(f'{n} x {4:2} = {t4}')
print(f'{n} x {5:2} = {t5}')
print(f'{n} x {6:2} = {t6}')
print(f'{n} x {7:2} = {t7}')
print(f'{n} x {8:2} = {t8}')
print(f'{n} x {9:2} = {t9}')
print(f'{n} x {10:2} = {t10}')
print('-' * 20)
