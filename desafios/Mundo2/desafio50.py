# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for impar, desconsidere-o.

s = 0
for i in range(1, 7):
    numeros = int(input(f'Digite o {i}º número inteiro: '))
    if numeros % 2 == 0:
        s += numeros
else:
    print(f'\n- A soma dos números pares da sequência digitada acima é \033[1;32m{s}\033[m.')

    # RASCUNHO:

# num1 = int(input('Digite o primeiro número inteiro: '))
# num2 = int(input('Digite o segundo número inteiro: '))
# num3 = int(input('Digite o terceiro número inteiro: '))
# num4 = int(input('Digite o quarto número inteiro: '))
# num5 = int(input('Digite o quinto número inteiro: '))
# num6 = int(input('Digite o sexto número inteiro: '))
# numeros = [num1, num2, num3, num4, num5, num6]
# print(numeros)
# for i in num1, num2, num3, num4, num5, num6:
# for i in numeros:
#     if numeros % 2 == 0 in numeros:
#         print(i, end=' ')
# if num2 % 2 == 0:
#     print(i, end=' ')
# if num1 or num2 or num3 or num4 or num5 or num6 % 2 == 0:

    # print(numeros)
    # numlist = [numeros]
    # for p in numlist:
    #     print(f'O número {numeros} é par.\n')
    #     # print(f'A soma dos números pares é {s}')
    # elif numeros % 2 == 1:
    #     print(f'O número {numeros} é impar.\n')
# else:
# print(f'Os números digitados foram {numlist}')
# print(numeros % 2 == 0, end=' ')
# s += numeros
