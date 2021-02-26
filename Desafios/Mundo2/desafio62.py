"""Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
ele disser que quer mostrar 0 TERMOS"""

PA = 1
progressao = -1
while progressao < 9:
    print(':::' * 35)
    termo = int(input('\033[1m- Insira o primeiro termo da Progressão Aritmética: '))
    razao = int(input('- Insira a razão da Progressão Aritmética:\033[m'))
    print(':::' * 35)
    while progressao < 9:
        progressao += 1
        PA = termo + razao * progressao
        # print(f'{PA}', end=' --> ')
        print(f'\033[1;33m{PA}\033[m', end=' --> ')
    if progressao < 10:
        print('\n', '===' * 35, sep='')
        opcao = int(input(f'\033[1m- OS 10 PRIMEIROS TERMOS DA PROGRESSÃO ARITMÉTICA ESTÃO ACIMA.'
                          f'\nEscolha o que deseja fazer agora:\n'
                          f'[ 0 ] PARA PARAR O PROGRAMA\n'
                          f'[ 1 ] PARA MOSTRAR OUTROS TERMOS\n'
                          f'- Digite a opção desejada:\033[m '))
        print('===' * 35)
        progressao = -1
        if opcao == 1:
            print('\033[1;32mVOCÊ OPTOU POR MOSTRAR OUTROS TERMOS.\033[m')
        else:
            print('\033[1;31mVOCÊ OPTOU POR PARAR O PROGRAMA.\033[m')
            break

# PA = 1
# progressao = -1
# while progressao < 9:
#     print(':::' * 35)
#     termo = int(input('- Insira o primeiro termo da Progressão Aritmética: '))
#     razao = int(input('- Insira a razão da Progressão Aritmética:'))
#     print(':::' * 35)
#     while progressao < 9:
#         progressao += 1
#         PA = termo + razao * progressao
#         print(f'{PA}', end=' --> ')
#         # print(f'\033[1m{PA}\033[m', end=' -> ')
#     if progressao < 10:
#         print('\n', '===' * 35, sep='')
#         opcao = int(input(f'- OS 10 PRIMEIROS TERMOS DA PROGRESSÃO ARITMÉTICA ESTÃO ACIMA.'
#                           f'\nEscolha o que deseja fazer agora:\n'
#                           f'[ 0 ] PARA PARAR O PROGRAMA\n'
#                           f'[ 1 ] PARA MOSTRAR OUTROS TERMOS\n'
#                           f'- Digite a opção desejada: '))
#         print('===' * 35)
#         progressao = -1
#         if opcao == 1:
#             print('Você optou por mostrar outros termos.')
#         else:
#             print('Você optou por parar o programa.')
#             break
