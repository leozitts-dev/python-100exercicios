# Exercício 006 - Dobro, Triplo, Raiz Quadrada
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz2 = n ** (1/2)
print(f'Você digitou {n} \nSeu dobro é {dobro} \nSeu triplo é {triplo} \nSua raiz quadrada é {raiz2: .2f}')
