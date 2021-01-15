# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores. (considerar a maioridade de 21 anos)

from datetime import date

ano = date.today().year
maior = 0
menor = 0

for i in range(1, 8):
    nascimento = int(input(f'Insira o ano de nascimento da \033[1m{i}ª\033[m pessoa: '))
    if ano - nascimento >= 21:
        maior += (nascimento / nascimento)
    else:
        menor += (nascimento / nascimento)
else:
    print(f'- \033[1m{menor:.0f} pessoa ainda não atingiram a maioridade\033[m.\n'
          f'- \033[1m{maior:.0f} pessoa já são maiores de idade\033[m.')

# from datetime import date
#
# ano = date.today().year
# maior = 0
# menor = 0
#
# for i in range(1, 8):
#     nascimento = int(input(f'Insira o ano de nascimento da {i}ª pessoa: '))
#     if ano - nascimento >= 21:
#         maior += (nascimento / nascimento)
#     else:
#         menor += (nascimento / nascimento)
# else:
#     print(f'- {menor:.0f} pessoas ainda não atingiram a maioridade.\n'
#           f'- {maior:.0f} pessoas já são maiores de idade.')
