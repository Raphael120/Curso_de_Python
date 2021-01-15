# AULA 13 - ESTRUTURA DE REPETIÇÃO "FOR"

# s = 0
# for c in range(1, 6):
#     valor = int(input('Insira um valor:'))
#     s += valor
# print(f'O somatório dos valores é {s}')
# + EXEMPLOS:
# i = int(input('INICIO:'))
# f = int(input('FIM:'))
# p = int(input('PASSO:'))
#
# for c in range(i, f+1, p):
#     print(c)
# print('FIM')

# Usando um objeto no range:
num = int(input('Digite um número: '))
for c in range(0, num + 1):
    print(c)
print('FIM')

# # contagem progressiva:
# for c in range(1, 6):
#     print(c)
# print('FIM')
#
# # contagem regressiva:
# for c in range(10, 0, -1):
#     print(c)
# print('FIM')
#
# # de 2 em 2:
# for c in range(0, 11, 2):
#     print(c)
#