# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas.
# - O nome com todas minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite o seu nome completo:'))
maiusculo = nome.upper()
minusculo = nome.lower()
qtdse = len(nome.replace(' ', '').strip())
# pode subtrair os espaços com nome.count(), subtraindo ele com o len(nome) len(nome)-nome.count(' ').
nsplit = nome.split()
pnome = len(nsplit[0])

print(f'Seu nome completo é: {nome}.\n'
      f'seu nome com todas as letras em maiúsculo: {maiusculo}.\n'
      f'Seu nome com todas as letras em minúsculo: {minusculo}.\n'
      f'Seu nome tem o total de {qtdse} letras\n'
      f'O seu primeiro nome tem {pnome} letras.')
