# Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.

from random import randint

n = 0
co = 0
print(':::' * 60)
for c in range(1, 501, 2):
    if c % 3 == 0:
        cor = randint(31, 37)
        print(f'\033[1;{cor}m{c}\033[m', end=" ")
        n += c
        co = co + 1
else:
    print('\n'
          '- Os números impares múltiplos de três estão acima.\n'
          f'- O resultado da soma dos {co} números é: \033[1m{n}\033[m')
