# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas vindas.

nome = input('\033[1;31mQual é o seu nome?\033[m')

print('\033[1;32mÉ um prazer te conhecer', nome, '!')
# ou
print('É um prazer te conhecer {}!'.format(nome))
# ou
print(f'É um prazer te conhecer {nome}!')
