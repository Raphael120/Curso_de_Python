# Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possiveis sobre ele

a1 = (input('\033[1;34mDigite algo:\033[m'))

print('\033[1;32m',a1)
print('\033[1;31mTipo primitivo:', type(a1))
print(f'É minusculo? {a1.islower()}')
print(f'É numérico? {a1.isnumeric()}')
print(f'É alfanumérico? {a1.isalnum()}')
print('É "alfabético"?', a1.isalpha())
print('É decimal?', a1.isdecimal())
print('É maiusculo?', a1.isupper())
print('Possui caracteres ASCII?', a1.isascii())
print('É um espaço?', a1.isspace())
print('Possui letras minúsculas e maiúsculas?', a1.istitle())
