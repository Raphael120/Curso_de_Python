# Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.

n = 0
print(':::' * 60)
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(f'\033[1m{c}\033[m', end=" ")
        n += c
else:
    print('\n'
          '- Os números impares múltiplos de três estão acima.\n'
          f'- O resultado da soma entre eles é: \033[1m{n}\033[m')
