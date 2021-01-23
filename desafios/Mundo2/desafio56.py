# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo.
# - Qual é o nome do homem mais velho.
# - Quantas mulheres têm menos de 20 anos.

media = 0
idvelho = []
idnome = []
maisvelho = []
nomeidade = []
idmulher = 0
# nomes = []
# idades = 0
# sexos = 0

# for i in range(1, 5):
#     print(':::' * 15)
#     nome = str(input('Insira seu nome: '))
#     idade = int(input('Insira sua idade: '))
#                      '[1] PARA SEXO MASCULINO.\n'
#                      '[2] PARA SEXO FEMININO.\n'
#                      '- Digite a opção desejada: '))
#     sexo = int(input('Insira seu sexo:\n'
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

# nomes = [input('Insira o primeiro nome:'), input('Insira o segundo nome:'),
#          input('Insira o terceiro nome:'), input('Insira o quarto nome:')]
# testando = input('Digite um nome: '), input('Digite um número: ')
# testando2 = input('Digite um nome: '),  input('Digite um número:')
# print(testando[1], testando2[1], max(testando[1], testando2[1]))
for n in range(1, 5):
    print(':::' * 20)
    # nomeidade = (input(f'Insira o {n}° nome: ')).upper().strip(), input('Insira a sua idade: ')
    nome = input(f'Insira o {n}° nome: ')
    idade = (input('Insira sua idade: '))
    sexo = int(input('Insira seu sexo:\n'
                     '[1] Para masculino\n'
                     '[2] Para feminino\n'
                     'Digite a opção desejada:'))
    media += int(idade) / 4
    # nomes = nome
    # mvelho = [nome], [idade]
    # pessoa = nome, idade, sexo
    if sexo == 1:  # in pessoa == '1':
        print(f'- {nome} é do sexo MASCULINO e tem {idade} ANOS.')
        idades = [max(idade)]
        nomes = [nome]
        # idvelho = int(max(list(nomeidade[1])))
        # print('nomeidade[1]:', max([nomeidade[1]]))
        # idade = max(idade)
        # nomes = [nome]
        # idades = max(idade)
        # idvelho += list((idades + nomes))  # "funcional"
        idvelho += list((idades + nomes))
        # print(max(idvelho))
        # idnome = idnome + nomes
        # nomeidade += nomes
        # maisvelho = idvelho + idnome
        # if nomes
        # idnome += nome  # , idvelho  # + max(idades)
    elif sexo == 2:  # in pessoa == '2':
        print(f'- {nome} é do sexo FEMININO e tem {idade} ANOS.')
        if int(idade) < 20:
            idmulher += str(sexo).count('2')
            # print(f'{n} mulheres tem menos de 20 anos.')
    else:
        print('ERRO AO CONTINUAR. VOCÊ INSERIU UMA OPÇÃO INVÁLIDA PARA O SEXO!')
        break
else:
    # A MÉDIA DE IDADE VAI AQUI!!!
    print('::::' * 20)
    print(f"- Média de idade do grupo: '{media:.0f} anos'\n"
          f"- Nome do homem mais velho do grupo: '{max(idvelho)}'\n"
          f"- Quantidade de mulheres que tem menos de 20 anos: '{idmulher}'")  # , nomeidade
    # f'- O homem mais velho do grupo tem {idvelho} anos e se chama {idnome}')
