# Desenvolva um programa que leia o primeiro termo e a razão de uma PA (Progressão Aritmética). No final, mostre os 10
# primeiros termos dessa progressão.

termo = int(input('Insira o primeiro termo da Progressão Aritmética: '))
razao = int(input('Insira a razão da Progressão Aritmética: '))

print('::' * 30)

print('\033[1m- Os 10 primeiros termos dessa progressão são:\033[m')
for i in range(0, 10):
    PA = termo + razao * i
    print(PA, end=' -> ')
else:
    print('FIM')
