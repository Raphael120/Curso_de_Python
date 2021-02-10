# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# radians: converte um valor em graus para radianos.
# degrees: converte um valor em radianos para graus.
# --------------------------------------------
# from math import sin as seno, cos as cosseno, tan as tangente, radians as radianos
# angulo = float(input('Digite o valor do ângulo:'))
# anrad = radianos(angulo)
# print(f'O seno do ângulo de {angulo}° é {seno(anrad):.2f}\n'
#       f'O cosseno do ângulo de {angulo}° é {cosseno(anrad):.2f}\n'
#       f'A tangente do ângulo de {angulo}° é {tangente(anrad):.2f}.')

from math import sin, cos, tan, radians

angulo = float(input('Digite o valor do ângulo:'))
anrad = radians(angulo)
print(f'O seno do ângulo de {angulo}° é {sin(anrad):.2f}\n'
      f'O cosseno do ângulo de {angulo}° é {cos(anrad):.2f}\n'
      f'A tangente do ângulo de {angulo}° é {tan(anrad):.2f}.')
