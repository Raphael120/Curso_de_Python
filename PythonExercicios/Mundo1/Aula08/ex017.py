# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
# mostre o comprimento da hipotenusa.

# # RESOLUÇÃO SEM 'math.hypot':

cttop = float(input('Digite o comprimento do cateto oposto:'))
cttadj = float(input("Digite o comprimento do cateto adjacente:"))
hipotenusa = (cttop ** 2 + cttadj ** 2)

print(f'O comprimento do cateto oposto é {cttop} centímetros,\n'
      f'O comprimento do cateto adjacente é {cttadj} centímetros,\n'
      f'o comprimento da hipotenusa é {hipotenusa**0.5:.2f} centímetros.')

print('-'*20)

# RESOLUÇÃO COM 'import math':

import math
ctop = float(input('Digite o comprimento do cateto oposto:'))
ctad = float(input('Digite o comprimento do cateto adjacente:'))
# math.hypot(ctop, ctad)
print(f'O comprimento do cateto oposto é {ctop} centímetros,\n'
      f'O comprimento do cateto adjacente é {ctad} centímetros,\n'
      f'O comprimento da hipotenusa é {math.hypot(ctop, ctad):.2f} centímetros.')

print('-'*20)

# RESOLUÇÃO COM 'from math import hypot':

from math import hypot as hipotenusa
ctop = float(input('Digite o comprimento do cateto oposto:'))
ctad = float(input('Digite o comprimento do cateto adjacente:'))
print(f'O comprimento do cateto oposto é {ctop} centímetros,\n'
      f'O comprimento do cateto adjacente é {ctad} centímetros,\n'
      f'O comprimento da hipotenusa é {hipotenusa(ctop, ctad):.2f} centímetros.')
