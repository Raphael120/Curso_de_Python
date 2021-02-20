"""Refaça o DESAFIO 051, lendo o PRIMEIRO TERMO e a RAZÃO de uma PA, mostrando os 10 PRIMEIROS TERMOS da progressão
usando a estrutura while."""

# LAÇO FOR:

"""termo = int(input('Insira o primeiro termo da Progressão Aritmética: '))
razao = int(input('Insira a razão da Progressão Aritmética: '))

print('::' * 30)

print('\033[1m- Os 10 primeiros termos dessa progressão são:\033[m')
for i in range(0, 10):
    PA = termo + razao * i
    print(PA, end=' -> ')
else:
    print('FIM')"""

# WHILE:

pts = -2
pts = pts + 1
termo = int(input('- Insira o primeiro termo da Progressão Aritmética: '))
razao = int(input('- Insira a razão da Progressão Aritmética: '))
print(':::' * 25)
print(f'\033[1m- Os 10 primeiros termos dessa progressão são:\033[m')
while pts < 9:
    pts += 1
    PA = termo + razao * pts
    print(PA, end=' -> ')
print('FIM')
