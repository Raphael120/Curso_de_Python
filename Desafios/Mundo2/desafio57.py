""" Faça um programa que leia o SEXO de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
digitação novamente até ter um valor correto."""

s = 'M'
while s != 'M' or s != 'F':
    s = str(input('Escolha o seu sexo:\n'
                  '- [ M ] Para sexo MASCULINO\n'
                  '- [ F ] Para sexo FEMININO\n'
                  '- Ou aperte ENTER para parar a execução do programa.\n'
                  'Escolha a opção desejada: ')).strip().upper()  # '[0]' <- Pode ser usado para pegar só a 1ª letra.
    print('---' * 20)
    if s == 'M':
        print('- Você escolheu o sexo MASCULINO.')
        break
    if s == 'F':
        print('- Você escolheu o sexo FEMININO.')
        break
    if s == '':
        print('\033[1;34mVOCÊ OPTOU POR FINALIZAR O PROGRAMA\033[m')
        break
    if s != 'M' or s != 'F' or s != '':
        print('\033[1;31mEscolha uma opção válida!\033[m')

# s = 'M'
# while s != 'M' or s != 'F':
#     s = str(input('Escolha o seu sexo:\n'
#                   '- [ M ] Para sexo MASCULINO\n'
#                   '- [ F ] Para sexo FEMININO\n'
#                   '- Ou aperte ENTER para parar a execução do programa.\n'
#                   'Escolha a opção desejada: ')).upper().strip()
#     print('---' * 20)
#     if s == 'M':
#         print('- Você escolheu o sexo MASCULINO.')
#         break
#     if s == 'F':
#         print('- Você escolheu o sexo FEMININO.')
#         break
#     if s == '':
#         print('VOCÊ OPTOU POR FINALIZAR O PROGRAMA')
#         break
#     if s != 'M' or s != 'F' or s != '':
#         print('Escolha uma opção válida!')

# RESOLUÇÃO DO DESAFIO:

'''sexo = str(input('- Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input('- Dados inválidos. Por favor, informe seu sexo: ')). strip().upper()[0]
print(f'- Sexo {sexo} registrado com sucesso.')'''
