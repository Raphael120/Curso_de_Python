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

'''primeiros_termos = -2
primeiros_termos = primeiros_termos + 1
termo = int(input('- Insira o primeiro termo da Progressão Aritmética: '))
razao = int(input('- Insira a razão da Progressão Aritmética: '))
print(':::' * 25)
print(f'\033[1m- Os 10 primeiros termos dessa progressão são:\033[m')
while primeiros_termos < 9:
    primeiros_termos += 1
    PA = termo + razao * primeiros_termos
    print(PA, end=' -> ')
print('FIM')'''

# RESOLUÇÃO (COM CONTADOR = 1):

termo = int(input('- Insira o primeiro termo da Progressão Aritmética: '))
razao = int(input('- Insira a razão da Progressão Aritmética: '))
contador = 1
PA = termo
print(':::' * 25)
print(f'\033[1m- Os 10 primeiros termos dessa progressão são:\033[m')
while contador <= 10:
    print(PA, end=' -> ')
    contador += 1
    PA += razao
print('FIM')
