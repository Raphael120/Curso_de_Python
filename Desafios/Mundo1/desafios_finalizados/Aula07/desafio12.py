# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto: R$'))

np = preco - (preco * 5) / 100

print(f'O produto custa R${preco}.')
print(f'Com um desconto de 5%, o produto custará R${np:.2f}.')


# ---------------------------------------------------------------------
# Prática com outra % de desconto:

# preco = float(input('Digite o preço do produto:'))
# desconto = float(input('Digite o valor do desconto (%):'))
# np = preco - (preco * desconto) / 100
#
# print(f'O produto tem o preço de R${preco}.')
# print(f'Com um desconto de {desconto}%, o produto custará R${np:.2f}.')
