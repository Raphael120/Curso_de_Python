# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

# OU
# for c in range(2, 51, 2):
#     print(c)
# for n in range(1, 50, 2):
#     print(n+1, end=" ")
# -------------------------------------------------------------------
for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')
else:
    print(f'\n\033[1m- Os números pares do intervalo de 1 a 50 estão acima.\033[m')
