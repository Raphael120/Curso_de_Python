# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar;
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

# from time import sleep
# USANDO A BIBLIOTECA DATETIME:
from datetime import date

print('\033[1mGERENCIADOR DE ALISTAMENTO MILITAR\033[m\n')

atual = date.today().year
genero = int(input('Escolha seu gênero:\n'
                   '- Digite [ 1 ] Para MASCULINO\n'
                   '- Digite [ 2 ] Para FEMININO\n'
                   'Digite a opção desejada: '))

if genero == 1:
    print(':::' * 30)
    nascimento = int(input('Insira o seu ano de nascimento:'))
    idade = atual - nascimento
    if idade < 18:
        print(f'- Estamos no ano de {atual} e você tem {idade} anos.\n'
              f'- Faltam {18 - idade} ano(s) para o alistamento militar.\n'
              f'- Você irá se alistar em {nascimento + 18}.')
    elif idade == 18:
        print(f'- Estamos no ano de {atual} e você tem já tem {idade} anos. '
              f'Está na hora de se alistar ao Serviço Militar.')
    else:
        print(f'- Estamos no ano de {atual} e você tem {idade} anos.\n'
              f'- Já se passaram {idade - 18} ano(s) do prazo de alistamento militar.\n'
              f'- Você deveria ter se alistado em {nascimento + 18}.')
elif genero == 2:
    print(':::' * 30)
    print('Você é do gênero feminino. O alistamento não é obrigatório.')
else:
    print(':::' * 30)
    print('Escolha uma opção válida.')

# SEM A BIBLIOTECA DATETIME:
#
# sleep(1)
# nascimento = int(input('Insira o ano do seu nascimento:'))
# idade = 2020 - nascimento
# sleep(1)
#
# if idade < 18:
#     print(f'Estamos em 2020 e você tem \033[1m{idade} anos\033[m. '
#           f'Irá se alistar no serviço militar em {2020 - idade + 18}.\n'
#           f'\033[1;32mFaltam {18 - idade} ano(s) para o alistamento militar.\033[m')
# elif idade == 18:
#     print(f'Estamos em 2020 e você já tem \033[1m{idade} anos\033[m. Está na hora de se alistar ao serviço militar.')
# else:
#     print(f'Estamos em 2020 e você já tem \033[1m{idade} anos\033[m. Seu alistamento foi em {2020 - idade + 18}.\n'
#           f'\033[1;31mJá se passou {idade - 18} ano(s) do tempo de alistamento!\033[m')
