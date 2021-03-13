# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

# Obs: Para que se possa construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma
# das medidas dos outros dois e maior que o valor absoluto da diferença entre essas medidas.
#  |b - c| < a < b + c

a = float(input('Digite o comprimento da reta "A":'))
b = float(input('Digite o comprimento da reta "B":'))
c = float(input('Digite o comprimento da reta "C":'))
AB = a + b
ABN = a - b
AC = a + c
ACN = a - c
BC = b + c
BCN = b - c

# print((b - c) < a < (b + c))
# print((a - c) < b < (a + c))
# print((a - b) < c < (a + b))
# if ABN < c < AB:
#     print('- Pode formar um Triângulo.')
# elif ACN < b < AC:
#     print('- Sim, podem formar um triângulo. ')
# elif BCN < a < BC:
#     print('- As retas podem formar um triângulo.')
# else:
#     print('As retas inseridas não podem formar um triângulo.')

if a < BC and b < AC and c < AB:
    print('- As retas podem formar um triângulo.')
# if b < AC:
#     print('- A soma das retas A e C é maior que a reta B, então elas podem formar um triângulo. ')
# if c < AB:
#     print('- As retas podem formar um triângulo.')
else:
    print('As retas inseridas não podem formar um triângulo.')
