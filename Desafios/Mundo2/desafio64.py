"""Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. O programa só vai parar quando o usuário digitar
o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag)"""

num = 0
soma = 0
contagem = 0

while num != 999:
    num = int(input("Digite um número inteiro (Digite '\033[1;31m999\033[m' para parar o programa): "))
    if num != 999:
        soma += num
        contagem += 1
else:
    print(':::' * 30)
    print(f'\033[1;33mVOCÊ OPTOU POR PARAR O PROGRAMA\033[m.\n'
          f'- Foram digitados \033[1;32m{contagem}\033[m números.\n'
          f'- A soma entre os números digitados é: \033[1;32m{soma}\033[m.')


# num = 0
# soma = 0
# contagem = 0
# while num != 999:
#     num = int(input("Digite um número inteiro (Digite '999' para parar o programa): "))
#     if num != 999:
#         soma += num
#         contagem += 1
# else:
#     print(':::' * 30)
#     print(f'VOCÊ OPTOU POR PARAR O PROGRAMA.\n'
#           f'- Foram digitados {contagem} números.\n'
#           f'- A soma entre os números digitados é {soma}.')
