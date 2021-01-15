# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número:6.127 - O número 6.127 tem a parte inteira 6.

import math
num = float(input('Digite um número Real:'))
num1 = math.trunc(num)
print(f'O número Real digitado foi {num} e sua parte inteira é: {num1}')
# ou
from math import trunc
num = float(input('Digite um número Real:'))
print(f'O número Real digitado foi {num} e sua parte inteira é  {trunc(num)}.')
# ou
num = float(input('Digite um número Real:'))
print(f'O número Real digitado foi {num} e sua parte inteira é {int(num)}')
