# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo.
# - Qual é o nome do homem mais velho.
# - Quantas mulheres têm menos de 20 anos.


# nomes = []
# idades = 0
# media = 0
# sexos = 0

# for i in range(1, 5):
#     print(':::' * 15)
#     nome = str(input('Insira seu nome: '))
#     idade = int(input('Insira sua idade: '))
#     sexo = int(input('Insira seu sexo:\n'
#                      '[1] PARA SEXO MASCULINO.\n'
#                      '[2] PARA SEXO FEMININO.\n'
#                      '- Digite a opção desejada: '))
#     media += idade / 4  # MÉDIA OK
#     nomes = nome
#     idades = idade
#     sexos = sexo
    # pass

# else:
#     # print(f'A média de idade do grupo é de: {media:.0f} anos.'  # MÉDIA OK
#     #       f'O nome do homem mais velho é  ')
#     print(nomes, idades, sexos)

# print(':::' * 15)
# print(nome, idade, sexo)

# testando

nomes = [input('Insira o primeiro nome:'), input('Insira o segundo nome:'),
         input('Insira o terceiro nome:'), input('Insira o quarto nome:')]

for n in nomes:
    print(n)