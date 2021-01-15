# Crie um programa que faça o computador jogar Jokempô com você.
# Pedra ganha da tesoura (amassando-a ou quebrando-a).
# Tesoura ganha do papel (cortando-o).
# Papel ganha da pedra (embrulhando-a).

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from random import choice
from time import sleep

print('\033[1;34m::::\033[m' * 30)
print('\033[1mPEDRA, PAPEL E TESOURA\033[m')
print('\033[1;34m::::\033[m' * 30)
jokempo = ('pedra', 'papel', 'tesoura')
humano = str(input('\033[1mEscolha PEDRA, PAPEL ou TESOURA:\033[m ')).upper().strip()
maquina = choice(jokempo).upper()
sleep(1)
# Caso escolher uma opção inválida:
if humano not in 'PEDRA' 'PAPEL' 'TESOURA':
    print('\033[1;31mESCOLHA UMA OPÇÃO VÁLIDA.\033[m')

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
print(f'- Você escolheu \033[1;33m{humano}\033[m e o computador escolheu \033[1;33m{maquina}\033[m.')
sleep(1)
# JOkEMPÔ:
if humano == maquina:
    print(f'- Os dois escolheram \033[1;33m{humano}\033[m. \033[1mEMPATE!\033[m')
# Pedra ganha da tesoura:
elif humano == 'PEDRA' and maquina == 'TESOURA':
    print('- \033[1;33mPEDRA\033[m quebra \033[1;33mTESOURA\033[m. \033[1;32mVOCÊ GANHOU!\033[m')
elif humano == 'TESOURA' and maquina == 'PEDRA':
    print('- \033[1;33mPEDRA\033[m quebra \033[1;33mTESOURA\033[m. \033[1;31mVOCÊ PERDEU!\033[m')
# Tesoura ganha do papel:
elif humano == 'TESOURA' and maquina == 'PAPEL':
    print('- \033[1;33mTESOURA\033[m corta \033[1;33mPAPEL\033[m. \033[1;32mVOCÊ GANHOU!\033[m')
elif humano == 'PAPEL' and maquina == 'TESOURA':
    print('- \033[1;33mTESOURA\033[m corta \033[1;33mPAPEL\033[m. \033[1;31mVOCÊ PERDEU!\033[m')
# Papel ganha da pedra:
elif humano == 'PAPEL' and maquina == 'PEDRA':
    print('- \033[1;33mPAPEL\033[m embrulha a \033[1;33mPEDRA\033[m. \033[1;32mVOCÊ GANHOU!\033[m')
elif humano == 'PEDRA' and maquina == 'PAPEL':
    print('- \033[1;33mPAPEL\033[m embrulha a \033[1;33mPEDRA\033[m. \033[1;31mVOCÊ PERDEU!\033[m')

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# from random import choice
#
# print('PEDRA, PAPEL E TESOURA')
#
# jokempo = ('pedra', 'papel', 'tesoura')
# humano = str(input('Escolha PEDRA, PAPEL ou TESOURA: ')).upper().strip()
# maquina = choice(jokempo).upper()
#
# # CASO ESCOLHER UMA OPÇÃO INVÁLIDA:
# if humano not in 'PEDRA' 'PAPEL' 'TESOURA':
#     print('Escolha uma opção válida.')
#
# print(':::::' * 20)
# print(f'- Você escolheu {humano} e o computador escolheu {maquina}.')
#
# # JOkEMPÔ:
# if humano == maquina:
#     print(f'- Os dois escolheram {humano}. EMPATE!')
# # PEDRA GANHA DA TESOURA:
# elif humano == 'PEDRA' and maquina == 'TESOURA':
#     print('- PEDRA quebra TESOURA. VOCÊ GANHOU!')
# elif humano == 'TESOURA' and maquina == 'PEDRA':
#     print('- PEDRA quebra TESOURA. VOCÊ PERDEU!')
# # TESOURA GANHA DO PAPEL:
# elif humano == 'TESOURA' and maquina == 'PAPEL':
#     print('- TESOURA corta PAPEL. VOCÊ GANHOU!')
# elif humano == 'PAPEL' and maquina == 'TESOURA':
#     print('- TESOURA corta PAPEL. VOCÊ PERDEU!')
# # PAPEL GANHA DA PEDRA:
# elif humano == 'PAPEL' and maquina == 'PEDRA':
#     print('- PAPEL embrulha a PEDRA. VOCÊ GANHOU!')
# elif humano == 'PEDRA' and maquina == 'PAPEL':
#     print('- PAPEL embrulha a PEDRA. VOCÊ PERDEU!')

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# OU:
# TAMBÉM PODE SER FEITO UTILIZANDO O RANDINT, COM AS OPÇÕES DE ESCOLHA 0, 1 E 2. SE SUBSTITUIR AS STRINGS 'PEDRA',
# 'PAPEL' E 'TESOURA' POR 0, 1 E 2 TAMBÉM FUNCIONA.
# from random import randint
#
# print('PEDRA, PAPEL E TESOURA')
#
# jokempo = ('PEDRA', 'PAPEL', 'TESOURA')
# maquina = randint(0, 2)
# # humano = str(input('Escolha PEDRA, PAPEL ou TESOURA: ')).upper().strip()
# humano = int(input('[ 0 ] PEDRA\n'
#                    '[ 1 ] PAPEL\n'
#                    '[ 2 ] TESOURA\n'
#                    'Qual é a sua escolha? '))
# print(f'O computador escolheu {jokempo[maquina]}.')
