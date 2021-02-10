# Escreva um programa que converta uma temperatura digitada em ºC para ºF

temp = float(input('Digite uma temperatura em Celsius:'))
Fah = (temp * 1.8) + 32

print(f'A temperatura inserida foi {temp:.1f}ºC, que é equivalente a {Fah:.1f}ºF.')
