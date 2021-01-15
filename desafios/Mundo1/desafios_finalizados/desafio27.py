# Faça um programa que leia o nome completo de uma pessoa e mostre em seguida o primeiro e o último nome separadamente.
# Ex:Ana Maria Souza
# primeiro = Ana
# Último = Souza

nome = input('Insira o nome completo desejado:').strip()
splitname = nome.split()

print(f'O nome inserido foi {nome}.\n'
      f'Primeiro nome: {splitname[0]}\n'
      f'Último nome: {splitname[-1]}')
