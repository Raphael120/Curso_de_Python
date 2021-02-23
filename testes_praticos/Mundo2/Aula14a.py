"""AULA 14 - ESTRUTURA DE REPETIÇÃO WHILE"""

'LAÇO FOR:'
# for c in range(1, 10):
#     print(c)
# else:
#     print('FIM')

# for c in range(1, 5):
#     n = int(input('Digite um número: '))
# else:
#     print('FIM')

'LAÇO WHILE:'
c = 1
while c < 11:
    print(c)
    c += 1
else:
    print('FIM')

# n = 1
# r = 'S'
# while r == 'S':  # <-- Isso é um FLAG (Ponto de parada / Condição de parada)
#     n = int(input('Digite um valor: '))
#     r = str(input('Quer continuar? [S/N] ')).upper().strip()
# else:
#     print('FIM')

# n = 1
# par = impar = 0
# while n != 0:
#     n = int(input('Digite um número (Digite 0 para parar a contagem): '))
#     if n != 0:
#         if n % 2 == 0:
#             par += 1
#         else:
#             impar += 1
# else:
#     print(f'Dentre os números digitados, {par} são pares e {impar} são impares.')

