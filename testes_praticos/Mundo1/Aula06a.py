# AULA 6 - TIPOS PRIMITIVOS E SAÍDAS DE DADOS

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite um valor:'))
s = n1 + n2

print('A soma entre', n1, 'e', n2, 'vale', s,)
# ou
print('A soma entre {} e {} vale {}'.format(n1, n2, s))
# ou
print(f'A soma entre {n1} e {n2} vale {s}')
