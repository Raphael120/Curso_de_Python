# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for impar, desconsidere-o.

s = 0
c = 0
for i in range(1, 7):
    numeros = int(input(f'Digite o {i}º número inteiro: '))
    if numeros % 2 == 0:
        s += numeros
        c = c + 1  # ou c += 1
else:
    print(f'Foi inserido {c} número(s) pares.'
          f'\n- A soma dos números pares da sequência digitada acima é \033[1;32m{s}\033[m.')
