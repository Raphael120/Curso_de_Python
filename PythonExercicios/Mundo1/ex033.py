# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# VERSÃO SEM O IF/ELSE:
num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número:'))
num3 = int(input('Digite o terceiro número:'))
numm = [num1, num2, num3]
print(min(numm), max(numm))
print(f'- Os números inseridos foram: {num1}, {num2} e {num3}.\n'
      f'- Maior número: {max(numm)}\n'
      f'- Menor número: {min(numm)}')
print('-=-' * 30)

# VERSÃO COM IF/ELSE:
# MENOR VALOR:
menor = num1
if num2 <= num1 and num3:
    menor = num2
if num3 <= num1 and num2:
    menor = num3
print(f'O menor valor é o número {menor}.')
# MAIOR VALOR:
maior = num1
if num2 >= num1 and num3:
    maior = num2
if num3 >= num2 and num1:
    maior = num3
print(f'O maior valor é o número {maior}.')
