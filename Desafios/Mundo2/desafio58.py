"""Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um NÚMERO ENTRE 0 E 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""

from random import randint
from time import sleep

numero = 0
while numero <= 100:
    print(':::' * 30)
    computador = randint(0, 10)
    num = int(input('Tente adivinhar o número pensado pelo computador!\n'
                    '- Escolha um número de 0 a 10: '))
    if num > 10 or num < 0:
        print('\n- \033[1;31mERRO AO CONTINUAR, ESCOLHA UM NÚMERO DE 0 A 10!\033[m')
        break
    if computador != num:
        numero += 1
        print(f'- Você escolheu o número \033[1;34m{num}\033[m e o computador pensou no '
              f'número \033[1;34m{computador}\033[m,'
              f' \033[1;31mTENTE NOVAMENTE!\033[m')
        sleep(0.5)
    if computador == num:
        print(':::' * 30)
        sleep(0.5)
        print(f'\033[1mVocê escolheu o mesmo número que o computador (Número {num})\033[m.\n'
              '- \033[1;32mVOCÊ GANHOU!\033[m\n'
              f'- \033[1mForam necessárias {numero + 1} tentativas para você acertar!\033[m')
        break

# from random import randint
# from time import sleep
#
# numero = 0
# while numero <= 100:
#     print(':::' * 30)
#     computador = randint(0, 10)
#     num = int(input('Tente adivinhar o número pensado pelo computador!\n'
#                     '- Escolha um número de 0 a 10: '))
#     if num > 10 or num < 0:
#         print('\n- ERRO AO CONTINUAR, ESCOLHA UM NÚMERO DE 0 A 10!')
#         break
#     if computador != num:
#         numero += 1
#         print(f'- Você escolheu o número {num} e o computador pensou no número {computador}, tente novamente!')
#         sleep(0.5)
#     if computador == num:
#         print(':::' * 30)
#         sleep(0.5)
#         print(f'Você escolheu o mesmo número que o computador (número {num}).\n'
#               '- VOCÊ GANHOU!\n'
#               f'- Foram necessárias {numero + 1} tentativas para você acertar!')
#         break

