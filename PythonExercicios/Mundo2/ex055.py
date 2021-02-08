# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.


p = []
for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}ª pessoa:'))
    p += [peso]
else:
    print(f'\nO menor peso lido foi: {min(p)}Kg\n'
          f'O maior peso lido foi: {max(p)}Kg')
