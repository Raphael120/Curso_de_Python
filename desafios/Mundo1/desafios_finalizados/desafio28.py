# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randrange as sorteio, randint as sorteioint
from time import sleep

# Programa n°1 (com 'randrange'):
print('-=-' * 25)
num = int(input('Qual foi o número inteiro, de 0 a 5, que foi escolhido pelo computador?'))
print('-=-' * 25)
print('PROCESSANDO...')
sleep(2)
num1 = sorteio(0, 6)
print(f'você escolheu o número {num}.\n'
      f'O computador pensou  no número {num1}, então:')

if num1 == num:
    print('Você venceu!')
else:
    print('Você perdeu, tente novamente.')
print('=-=' * 25)

# Programa n° 2 (com 'randint'):
num2 = sorteioint(0, 5)
print(f'Você pensou no número {num} e o computador no número {num2}, então:')

if num2 == num:
    print('VOCÊ VENCEU!')
else:
    print('VOCÊ PERDEU.')
