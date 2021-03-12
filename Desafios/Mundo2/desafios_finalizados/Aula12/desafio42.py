# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais.
# - Isósceles: dois lados iguais.
# - Escaleno: todos os lados diferentes.

# a = float(input('\033[1mInsira o comprimento da reta "A": '))
# b = float(input('Insira o comprimento da reta "B": '))
# c = float(input('Insira o comprimento da reta "C":\033[m '))

# if a < (b + c) and b < (a + c) and c < (a + b):
#     print('- \033[1;32mAs retas podem formar um triângulo.\033[m')
#     # if a != b and a != c and b != c:
#     # OU:
#     if a != b != c != a:
#         print('- Podem formar um triângulo do tipo \033[1;33mESCALENO\033[m.')
#     # if a == b and a == c and b == c:
#         # OU:
#     elif a == b == c:
#         print('- Podem formar um triângulo do tipo \033[1;33mEQUILÁTERO\033[m.')
#     # elif a == b or a == c or b == c:
#     else:
#         print('- Podem formar um triângulo do tipo \033[1;33mISÓSCELES\033[m.')
# else:
#     print('\033[1;31mAs retas inseridas não podem formar um triângulo.\033[m')


a = float(input('Insira o comprimento da reta "A": '))
b = float(input('Insira o comprimento da reta "B": '))
c = float(input('Insira o comprimento da reta "C": '))

if a < (b + c) and b < (a + c) and c < (a + b):
    print('- As retas podem formar um triângulo.')
    if a != b and a != c and b != c:
        print('- Podem formar um triângulo do tipo ESCALENO.')
    elif a == b and a == c and b == c:
        print('- Podem formar um triângulo do tipo EQUILÁTERO.')
    else:
        print('- Podem formar um triângulo do tipo ISÓSCELES.')
else:
    print('As retas inseridas não podem formar um triângulo.')
