"""Faça um programa que leia um número qualquer e mostre o seu fatorial.
EX: 5! = 5x4x3x2x1 = 120   (FAZER O EXERCÍCIO USANDO O LAÇO FOR E O WHILE)"""

# LAÇO FOR:

fatorial = 1
f = 0
num = int(input('Insira um número para mostrar o seu fatorial: '))
for i in range(num, 0, -1):
    fatorial *= i
    f = i
    print(i, end=' x ')
print(f'\n{num}! = {fatorial}')
