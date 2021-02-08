# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores. (considerar a maioridade de 21 anos)

from datetime import date

ano = date.today().year
maior = 0
menor = 0

for i in range(1, 8):
    nascimento = int(input(f'Insira o ano de nascimento da \033[1m{i}ª\033[m pessoa: '))
    if ano - nascimento >= 21:
        maior += 1
    else:
        menor += 1
else:
    print(f'- \033[1m{menor} pessoa(s) ainda são menores de idade\033[m.\n'
          f'- \033[1m{maior} pessoa(s) já são maiores de idade\033[m.')

# from datetime import date
#
# ano = date.today().year
# maior = 0
# menor = 0
#
# for i in range(1, 8):
#     nascimento = int(input(f'Insira o ano de nascimento da {i}ª pessoa: '))
#     if ano - nascimento >= 21:
#         maior += 1
#     else:
#         menor += 1
# else:
#     print(f'- {menor:.0f} pessoa(s) ainda são menores de idade.\n'
#           f'- {maior:.0f} pessoa(s) já são maiores de idade.')
