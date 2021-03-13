# Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possiveis sobre ele

a1 = (input('Digite algo:'))

print(a1)
print('Tipo primitivo:', type(a1))
print('É minusculo?', a1.islower())
print('É numérico?', a1.isnumeric())
print('É alfanumérico?', a1.isalnum())
print('É "alfabético"?', a1.isalpha())
print('É decimal?', a1.isdecimal())
print('É maiusculo?', a1.isupper())
print('Possui caracteres ASCII?', a1.isascii())
print('É um espaço?', a1.isspace())
print('Possui letras minúsculas e maiúsculas?', a1.istitle())
