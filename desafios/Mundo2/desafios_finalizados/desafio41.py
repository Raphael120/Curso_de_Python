# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER

from datetime import date

nascimento = int(input('\033[1mInsira seu ano de nascimento:\033[m '))
idade = date.today().year - nascimento

if idade <= 9:
    print(f'- Você tem \033[1;32m{idade}\033[m anos e pertence a categoria \033[1;33mMIRIM\033[1m.')
elif idade <= 14:
    print(f'- Você tem \033[1;32m{idade}\033[m anos e pertence a categoria \033[1;33mINFANTIL\033[m.')
elif idade <= 19:
    print(f'- Você tem \033[1;32m{idade}\033[m anos e pertence a categoria \033[1;33mJUNIOR\033[m.')
elif idade <= 25:
    print(f'- Você tem \033[1;32m{idade}\033[m anos e pertence a categoria \033[1;33mSÊNIOR\033[m.')
else:
    print(f'- Você tem \033[1;32m{idade}\033[m anos. Pertence a categoria \033[1;33mMASTER\033[m '
          f'por ter ultrapassado os 20 anos.')
