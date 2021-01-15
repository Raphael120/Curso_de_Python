# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão.
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal
from time import sleep

print('-=-' * 35)
print('\033[1mCONVERSOR DE NÚMEROS INTEIROS\033[m')
print('-=-' * 35)
sleep(1.5)

numero = int(input('\033[1m- Digite o número inteiro desejado:\033[m '))
print(f'O número inserido foi \033[1;32m{numero}\033[m.')
print('-=-' * 35)
sleep(1.5)

opcao = int(input('- Para converter o número em \033[1;33mBINÁRIO\033[m, DIGITE \033[1;32m"1"\033[m.\n'
                  '- Para converter o número para \033[1;33mOCTAL\033[m, DIGITE \033[1;32m"2"\033[m.\n'
                  '- Para converter o número para \033[1;33mHEXADECIMAL\033[m, DIGITE \033[1;32m"3"\033[m.\n'
                  '\033[1mDigite a opção desejada\033[m: '))
print('-=-' * 35)
sleep(1.5)

if opcao == 1:
    print(f'- O número será convertido para \033[1;33mBINÁRIO\033[m.\n'
          f'- O número \033[1;32m{numero}\033[m convertido para \033[1;33mBINÁRIO\033[m é:'
          f' \033[1;32m{bin(numero).lstrip("0b")}\033[m')
elif opcao == 2:
    print(f'- O número será convertido para \033[1;33mOCTAL\033[m.\n'
          f'- O número \033[1;32m{numero}\033[m convertido para \033[1;33mOCTAL\033[m é:'
          f' \033[1;32m{oct(numero).lstrip("0o")}\033[m')
elif opcao == 3:
    print(f'- O número será convertido para \033[1;33mHEXADECIMAL\033[m.\n'
          f'- O número \033[1;32m{numero}\033[m convertido para \033[1;33mHEXADECIMAL\033[m é:'
          f' \033[1;32m{hex(numero).lstrip("0x").upper()}\033[m')
else:
    print('\033[1;31mErro ao converter número. Você não escolheu uma opção válida.\033[m')
print('-=-' * 35)


# from time import sleep
#
# print('-=-' * 20)
# print('CONVERSOR DE NÚMEROS INTEIROS')
# print('-=-' * 20)
# sleep(1.5)
#
# numero = int(input('- Digite o número inteiro desejado: '))
# print(f'O número inserido foi {numero}.')
# print('-=-' * 20)
# sleep(1.5)
#
# opcao = int(input('- Para converter o número em BINÁRIO, DIGITE "1".\n'
#                   '- Para converter o número para OCTAL, DIGITE "2".\n'
#                   '- Para converter o número para HEXADECIMAL, DIGITE "3".\n'
#                   'Digite a opção desejada: '))
# print('-=-' * 20)
# sleep(1.5)
#
# if opcao == 1:
#     print(f'- O número será convertido para BINÁRIO.\n'
#           f'- O número {numero} convertido para BINÁRIO é: {bin(numero).lstrip("0b")}')
# elif opcao == 2:
#     print(f'- O número será convertido para OCTAL.\n'
#           f'- O número {numero} convertido para OCTAL é: {oct(numero).lstrip("0o")}')
# elif opcao == 3:
#     print(f'- O número será convertido para HEXADECIMAL.\n'
#           f'- O número {numero} convertido para HEXADECIMAL é: {hex(numero).lstrip("0x").upper()}')
# else:
#     print('Erro ao converter número. Você não escolheu uma opção válida.')
