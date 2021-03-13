# Crie um programa que leia dois números e mostre a soma entre eles.

print('\033[1;36;m===== DESAFIO 03 =====\033[m')

numero1 = int(input('\033[32mPrimeiro número:'))
numero2 = int(input('\033[33mSegundo número:'))
s = numero1 + numero2

print('A soma é''\033[1;34m', s)

# ou (sem o int no numero1 e numero2):
# print('A soma é', int(numero1) + int(numero2))
