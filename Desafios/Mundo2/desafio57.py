""" Faça um programa que leia o SEXO de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
digitação novamente até ter um valor correto."""

s = 'M'
while s:
    if s == 'M' or s == 'F':
        s = str(input('Escolha o seu sexo:\n'
                      '- [ M ] Para sexo MASCULINO\n'
                      '- [ F ] Para sexo FEMININO\n'
                      '- Ou aperte ENTER para parar a execução do programa.\n'
                      'Digite a opção desejada: ')).upper().strip()
        print('---' * 20)
    elif s != 'M' or s != 'F':
        print('\033[1;31mEscolha uma opção válida!\033[m\n')
        s = str(input('Escolha o seu sexo:\n'
                      '- [ M ] Para sexo MASCULINO\n'
                      '- [ F ] Para sexo FEMININO\n'
                      '- Ou aperte ENTER para parar a execução do programa.\n'
                      'Digite a opção desejada: ')).upper().strip()
        print('---' * 20)
else:
    print('\033[1;34mVOCÊ OPTOU POR FINALIZAR O PROGRAMA\033[m')

# s = 'M'
# while s:
#     if s == 'M' or s == 'F':
#         s = str(input('Escolha o seu sexo:\n'
#                       '- [ M ] Para sexo MASCULINO\n'
#                       '- [ F ] Para sexo FEMININO\n'
#                       '- Ou aperte ENTER para parar a execução do programa.\n'
#                       'Digite a opção desejada: ')).upper().strip()
#         print('---' * 20)
#     elif s != 'M' or s != 'F':
#         print('Escolha uma opção válida!\n')
#         s = str(input('Escolha o seu sexo:\n'
#                       '- [ M ] Para sexo MASCULINO\n'
#                       '- [ F ] Para sexo FEMININO\n'
#                       '- Ou aperte ENTER para parar a execução do programa.\n'
#                       'Digite a opção desejada: ')).upper().strip()
#         print('---' * 20)
# else:
#     print('VOCÊ OPTOU POR FINALIZAR O PROGRAMA')
