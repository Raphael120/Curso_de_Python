"""Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um NÚMERO ENTRE 0 E 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""

from random import randint
from time import sleep
# print(randint(1, 10))

numero = 0
while numero <= 100:
    print(':::' * 30)
    computador = randint(0, 10)
    num = int(input('Tente adivinhar o número pensado pelo computador!\n'
                    '- Escolha um número de 0 a 10: '))
    if num > 10:
        print('\n- ERRO AO CONTINUAR, ESCOLHA UM NÚMERO DE 0 A 10!')
        break
    if computador != num:
        numero += 1
        print(f'- Você pensou no número {num} e o computador pensou no número {computador}, tente novamente!')
        sleep(0.5)
    if computador == num:
        print(':::' * 30)
        sleep(0.5)
        print(f'Você escolheu o mesmo número que o computador (número {num}).\n'
              '- VOCÊ GANHOU!\n'
              f'- Foram necessárias {numero + 1} tentativas para você acertar!')
        break

