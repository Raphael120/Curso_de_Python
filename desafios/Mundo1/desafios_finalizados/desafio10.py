# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$1.00 = R$3.27.

carteira = float(input('Digite um valor em reais: R$'))

# dólar = carteira / 3.27
#
# print(f'Você tem R${carteira:.2f} na carteira e pode comprar {dólar:.2f} dólares.')

# Prática com cotação atual:

dólar = carteira / 5.38
euro = carteira / 6.37
libra = carteira / 7.14

print(f'Você tem R${carteira:.2f} na carteira. Levando em consideração cotação do dia 20/11/2020, você pode comprar:\n'
      f'- Dólares: ${dólar:.2f}.\n'
      f'- Euros: €{euro:.2f}.\n'
      f'- Libras: £{libra:.2f}.\n'
      )
