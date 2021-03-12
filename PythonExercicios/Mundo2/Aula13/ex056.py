# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo.
# - Qual é o nome do homem mais velho.
# - Quantas mulheres têm menos de 20 anos.

media = 0
idvelho = 0
maisvelho = ''
idmulher = 0

for n in range(1, 5):
    print(f':::::::::::::: {n}ª PESSOA :::::::::::::')
    nome = str(input(f'Insira o {n}° nome: ')).strip().upper()
    idade = int(input('Insira sua idade: '))
    sexo = int(input('Insira seu sexo:\n'
                     '[1] Para masculino\n'
                     '[2] Para feminino\n'
                     'Digite a opção desejada: '))
    media += idade / 4
    if n == 1 and sexo == 1:
        print(f'- {nome} é do sexo MASCULINO e tem {idade} ANOS.')
        idvelho = idade
        maisvelho = nome
    if sexo == 1 and idade > idvelho:
        print(f'- {nome} é do sexo MASCULINO e tem {idade} ANOS.')
        idvelho = idade
        maisvelho = nome
    if sexo == 2:
        print(f'- {nome} é do sexo FEMININO e tem {idade} ANOS.')
        if idade < 20:
            idmulher += 1
    if sexo > 2 or sexo == 0:
        print('ERRO AO CONTINUAR. VOCÊ INSERIU UMA OPÇÃO INVÁLIDA PARA O SEXO!')
        break
else:
    print('---' * 20)
    print(f"- A média de idade do grupo é de {media:.0f} anos.\n"
          f"- A idade do homem mais velho é {idvelho} anos e seu nome é {maisvelho}.\n"
          f"- {idmulher} mulher(es) tem menos de 20 anos.")
