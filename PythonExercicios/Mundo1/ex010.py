# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$1.00 = R$3.27.

carteira = float(input('\033[4mDigite um valor em reais: R$\033[m'))

# dólar = carteira / 3.27
#
# print(f'Você tem R${carteira:.2f} na carteira e pode comprar {dólar:.2f} dólares.')

# Prática com cotação atual:

dólar = carteira / 5.38
euro = carteira / 6.37
libra = carteira / 7.14

print(f'Você tem \033[1;32mR${carteira:.2f}\033[m na carteira.\033[m'
      f'Levando em consideração cotação do dia \033[4m20/11/2020\033[m, você pode comprar:\n'
      f'- Dólares: \033[1;32m${dólar:.2f}\033[m.\n'
      f'- Euros: \033[1;32m€{euro:.2f}\033[m.\n'
      f'- Libras: \033[1;32m£{libra:.2f}\033[m.\n'
      )
