# Exercício 008 - Conversor de Medidas
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input('Digite o valor em metros: '))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000

print(f'O valor de {n:.0f}m')
print(f'Em Quilômetros é {km:.2f}km')
print(f'Em Hectômetros é {hm:.2f}hm')
print(f'Em Decâmetros é {dam:.0f}dam')
print(f'Em Decímetros é {dm:.0f}dm')
print(f'Em Centímetros é {cm:.0f}cm')
print(f'Em milímetros é {mm:.0f}mm')
