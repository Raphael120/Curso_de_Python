# refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('\033[1mInsira um número inteiro para mostrar a sua tabuada:\033[m '))

# SOMA:
print(f'\n\033[1m- A tabuada de soma do número \033[1;32m{num}\033[m é:\033[m\n')
for i in range(1, 11):
    print(f'\033[1m{num} + {i:2} = {num + i}\033[m')

# SUBTRAÇÃO:
print(f'\n\033[1m- A tabuada de subtração do número \033[1;32m{num}\033[m é:\033[m\n')
for i in range(1, 11):
    print(f'\033[1m{num} - {i:2} = {num - i}\033[m')

# MULTIPLICAÇÃO:
print(f'\n\033[1m- A tabuada de multiplicação do número \033[1;32m{num}\033[m é:\033[m\n')
for i in range(1, 11):
    print(f'\033[1m{num} X {i:2} = {num * i}\033[m')

# DIVISÃO:
print(f'\n\033[1m- A tabuada de divisão do número \033[1;32m{num}\033[m é:\033[m\n')
for i in range(1, 11):
    print(f'\033[1m{num} / {i:2} = {num / i:.1f}\033[m')
