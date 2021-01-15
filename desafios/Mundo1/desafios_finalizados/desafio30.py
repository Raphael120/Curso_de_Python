# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um número inteiro:'))

print(f'O número digitado foi: {num}.')

if num % 2 == 0:
    print('Esse número é par.')
else:
    print('Esse número é impar.')
