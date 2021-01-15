# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
# ex: Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

while True:
    try:
        num = (input('Insira um número de 0 a 9999:'))
        print(f'O número inserido foi {num}, sendo:')
        print('unidade:', num[-1])
        print('dezena:', num[-2])
        print('centena:', num[-3])
        print('milhar:', num[-4])
        break
    except IndexError:
        break


numint = int(input('Digite um número de 0 a 9999:'))

u = numint // 1 % 10
d = numint // 10 % 10
c = numint // 100 % 10
m = numint // 1000 % 10

print(f'O número inserido foi {numint}, sendo:\n'
      f'Unidade: {u}\n'
      f'Dezena: {d}\n'
      f'Centena: {c}\n'
      f'Milhar: {m}')

# print(f'O número inserido foi {num}...')
# print(f'unidade: {numl[:]}')
# print(f'dezena: {numl[:]}')
# print(f'centena: {numl[:]}')
# print(f'milhar: {numl[:]}')
