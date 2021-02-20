"""Faça um programa que leia um número qualquer e mostre o seu fatorial.
EX: 5! = 5x4x3x2x1 = 120   (FAZER O EXERCÍCIO USANDO O LAÇO FOR E O WHILE)"""

# LAÇO FOR:

fatfor = 1
f = 0
print(':::' * 20)
num = int(input('- Insira um número para mostrar o seu fatorial: '))
for i in range(num, 0, -1):
    fatfor *= i
    f = i
print(f'{num}! = {fatfor}')
print(':::' * 20)


# LAÇO WHILE:
fatwhile = 1
# print(':::' * 20)
num = int(input('- Insira um número para mostrar o seu fatorial: '))
fatnum = num
num = num + 1
while num != 1:
    num -= 1
    fatwhile *= num
print(f'{fatnum}! = {fatwhile}')
print(':::' * 20)
