"""Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
ele disser que quer mostrar 0 TERMOS"""

# termo = int(input('- Insira o primeiro termo da Progressão Aritmética: '))
# razao = int(input('- Insira a razão da Progressão Aritmética: '))
# print(':::' * 25)
#
# print(f'\033[1m- Os 10 primeiros termos dessa progressão são:\033[m')
# progressao = -1  # (PTS SIGNIFICA PRIMEIROS TERMOS)
# # progressao = progressao + 1
# while progressao < 9:
#     progressao += 1
#     PA = termo + razao * progressao
#     print(PA, end=' -> ')
# print('FIM')
# print(':::' * 25)
# opcao = int(input(f'- A Progressão Aritmética do número {termo} está acima.\n'
#                   f'Escolha o que deseja fazer agora:\n'
#                   f'[ 0 ] PARA PARAR O PROGRAMA\n'
#                   f'[ 1 ] PARA MOSTRAR OUTROS TERMOS\n'
#                   f'- Digite a opção desejada: '))
# if opcao == 1:
#     print(':::' * 25)
#     print('- Você optou por mostrar outros termos.')
#     termo1 = int(input('- Insira o primeiro termo da Progressão Aritmética: '))
#     razao1 = int(input('- Insira a razão da Progressão Aritmética: '))
#     progressao1 = -1
#     while progressao1 < 9:
#         progressao1 += 1
#         PA = termo1 + razao1 * progressao1
#         print(PA, end=' -> ')
#     print('FIM')
# elif opcao == 0:
#     print(':::' * 25)
#     print('- Você optou por parar o programa.')
# else:
#     print(':::' * 25)
#     print('- Você escolheu uma opção inválida.')

progressao = -1
PA = 1
# resultado = 0
while progressao <= 9:
    termo = int(input('- Insira o primeiro termo da Progressão Aritmética: '))
    razao = int(input('- Insira a razão da Progressão Aritmética: '))
    progressao += 1
    PA = termo + razao * progressao
    # break
print(PA, end = ' ')
# print(progressao)
# print(progressao)
