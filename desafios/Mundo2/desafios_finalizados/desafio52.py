# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# (2, 3, 5, 7)
# Exemplos:
#
# 1) O número 161:
# não é par, portanto não é divisível por 2;
# 1+6+1 = 8, portanto não é divisível por 3;
# não termina em 0 nem em 5, portanto não é divisível por 5;
# por 7:  161 / 7 = 23, com resto zero, logo 161 é divisível por 7, e portanto não é um número primo.

# 2) O número 113:
# não é par, portanto não é divisível por 2;
# 1+1+3 = 5, portanto não é divisível por 3;
# não termina em 0 nem em 5, portanto não é divisível por 5;
# por 7:  113 / 7 = 16, com resto 1. O quociente (16) ainda é maior que o divisor (7).
# por 11:  113 / 11 = 10, com resto 3. O quociente (10) é menor que o divisor (11), e além disso o resto é diferente de
# zero (o resto vale 3), portanto 113 é um número primo.

# for i in range(2, 101):
#     for x in range(2, i):
#         if i % x == 0:
#             print(f'\033[1;31m{i} NÃO é primo.\033[m')
#             break
#     else:
#         print(f'\033[1;32m{i} é PRIMO.\033[m')

# for i in range(2, 101):
#     for x in range(2, i):
#         if i % x == 0:
#             print(f'{i} NÃO é primo.')
#             break
#     else:
#         print(f'{i} é PRIMO.')

# RESOLUÇÃO:

num = int(input('Insira um número inteiro: '))
n = 0
for i in range(1, num + 1):
    # print(i, end=' ')
    if num % i == 0:
        print(f'\033[32m{i}\033[m', end=' ')
        n += 1
    else:
        print(f'\033[31m{i}\033[m', end=' ')
if n == 2:
    print(f'\n- O número {num} foi divisível {n} vezes, portanto ele \033[;32mÉ PRIMO.\033[m')
else:
    print(f'\n- O número {num} foi divisível {n} vezes, portanto ele \033[;31mNÃO É PRIMO.\033[m')
