"""Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma
SEQUÊNCIA DE FIBONACCI.
Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21 - 34...
Fórmula: (Fn = Fn - 1 + Fn - 2), (F(n + 2) = F(n + 1) + F(n))"""


# FIBONACCI 01:
# f, i = 0, 1
# fibo = int(input('Digite um número para mostrar o seu intervalo da sequência de Fibonacci: '))
# while f < fibo:
#     print(f, end=' ')
#     f, i = i, f + i
#     # print(fibo)

# # FIBONACCI DO DESAFIO:
fibo = int(input('Digite um número para mostrar a sua sequência de Fibonacci: '))
f, i = fibo, fibo + 1
while f == fibo:
    print(f, end=' ')
    f, i = f, f + i
    # print(fibo)

"""while True:
    # while f < 2:
    fn1 = int(input('Insira um número inteiro para mostrar a sua sequência de Fibonacci: '))
    f = 1
    fibo = (fn1 - 1) + (fn1 - 2)
    # fibo2 = fn * (fn + 1) + fn * fn
    # fn2 = fn1 + 1
    # fn3 = fn1 + fn2
    # fn3 = fn2 + fn1
    # print(fibo)
    while True:
        # while f < 100:
        f += fibo
        '''f += fn1
        f += fn2
        f += fn3'''
        # f += 1
        # f += f
        # f += i
        # f += b
        print(f, end=' ')
        # print(fn, fn1, fn2, end=' ')
        # print(fn)
        # print(f, end=' ')
        # fibo = n0 * n1 * n2 * f
        # print(fibo)
        # fibo
        # print(n0, n1, n2, end=' ')
        # print(n0, n1, n2, end=' ')"""
