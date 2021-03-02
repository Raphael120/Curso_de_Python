"""Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma
SEQUÊNCIA DE FIBONACCI.
Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21 - 34..."""
'Fórmula: (Fn = Fn - 1 + Fn - 2), (F(n + 2) = F(n + 1) + F(n))'


# fibo = n0, n1, n2
f = 0
# fn = 1
# f0 = 1
# f1 = 1
# f2 = 1
while f < 9:
    fn = int(input('Insira um número inteiro para mostrar a sua sequência de Fibonacci: '))
    # fn = (fn - 1) + (fn - 2)
    # n1 = n0 + 1
    # n2 = n0 + n1
    # n3 = n2 + n1
    while f < 100:
        f += 1
        # fib = f / fn
        print((f - 1) + (f - 2), end=' ')
        # if fib == 0.61:
            # print(f, end=' ')
            # print(fn, end=' ')
        # print(fn)
        # print(f, end=' ')
        # f0 += n0
        # f1 += n1
        # f2 += n2
        # fibo = n0 * n1 * n2 * f
        # print(fibo)
        # fibo
        # print(n0, n1, n2, end=' ')
        # print(n0, n1, n2, end=' ')

