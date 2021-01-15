# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento:
# - À vista dinheiro/cheque: 10% de desconto.
# - À vista no cartão: 5% de desconto.
# - Em até 2x no cartão: preço normal.
# - 3x ou mais  no cartão: 20% de juros.

# from time import sleep
#
# preco = float(input('\033[1mInsira o preço do produto: R$\033[m'))
# sleep(0.8)
# print('\033[1m::::\033[m' * 25)
# condicao = float(input('\033[1mEscolha a condição de pagamento:\033[m\n'
#                        '- Para pagar à vista com dinheiro ou cheque \033[1;33m(com 10% de desconto)\033[m,'
#                        ' DIGITE \033[1;34m"1"\033[m.\n'
#                        '- Para pagar à vista no cartão \033[1;33m(com 5% de desconto)\033[m,'
#                        ' DIGITE \033[1;34m"2"\033[m.\n'
#                        '- Para pagar em até 2x no cartão \033[1;33m(preço normal)\033[m,'
#                        ' DIGITE \033[1;34m"3"\033[m.\n'
#                        '- Para pagar em 3x ou mais no cartão \033[1;33m(com 20% de juros)\033[m,'
#                        ' DIGITE \033[1;34m"4"\033[m.\n'
#                        '\033[1mInsira a opção desejada:\033[m'))
# sleep(0.8)
# print('\033[1m::::\033[m' * 25)
# if condicao == 1:
#     print(f'O produto custa \033[1;32mR${preco:.2f}\033[m e você escolheu pagar à vista com dinheiro ou cheque.\n'
#           f'Com \033[1;33m10% de desconto\033[m, o produto custará:'
#           f' \033[1;32mR${preco - (preco * 10 / 100):.2f}\033[m. ')
# elif condicao == 2:
#     print(f'O produto custa \033[1;32mR${preco:.2f}\033[m e você escolheu pagar à vista no cartão.\n'
#           f'Com \033[1;33m5% de desconto\033[m, o produto custará: \033[1;32mR${preco - (preco * 5 / 100):.2f}\033[m.')
# elif condicao == 3:
#     print(f'O produto custa \033[1;32mR${preco:.2f}\033[m e você escolheu pagar em até 2x no cartão.')
# elif condicao == 4:
#     print(f'O produto custa \033[1;32mR${preco:.2f}\033[m e você escolheu pagar em 3x ou mais no cartão.\n'
#           f'Com \033[1;33m20% de juros\033[m, o produto custará: \033[1;32mR${preco + (preco * 20 / 100):.2f}\033[m.')
# else:
#     print('\033[1;31mErro ao calcular o preço do produto. A opção inserida é inválida.\033[m')


preco = float(input('Insira o preço do produto: R$'))
print('::::' * 25)
condicao = float(input('Escolha a condição de pagamento:\n'
                       '- [ 1 ] Para pagar à vista com dinheiro ou cheque (com 10% de desconto).\n'
                       '- [ 2 ] Para pagar à vista no cartão (com 5% de desconto).\n'
                       '- [ 3 ] Para pagar em até 2x no cartão (preço normal).\n'
                       '- [ 4 ] Para pagar em 3x ou mais no cartão (com 20% de juros).\n'
                       'Digite a opção desejada:'))
print('::::' * 25)
if condicao == 1:
    print(f'- O produto custa R${preco:.2f} e você escolheu pagar à vista com dinheiro ou cheque.\n'
          f'- Com 10% de desconto, o produto custará: R${preco - (preco * 10 / 100):.2f}. ')
elif condicao == 2:
    print(f'- O produto custa R${preco:.2f} e você escolheu pagar à vista no cartão.\n'
          f'- Com 5% de desconto, o produto custará: R${preco - (preco * 5 / 100):.2f}.')
elif condicao == 3:
    print(f'- O produto custa R${preco:.2f} e você escolheu pagar em 2x de R${preco / 2:.2f} no cartão.')
elif condicao == 4:
    parcela = int(input('Em quantas parcelas? '))
    if parcela < 3:
        print('Erro ao parcelar produto. Escolha um número válido de parcelas.')
    else:
        print(f'- O produto custa R${preco:.2f} e você escolheu pagar em 3x ou mais no cartão.\n'
              f'- Com 20% de juros, o produto custará: R${preco + (preco * 20 / 100):.2f}.\n'
              f'- Você escolheu pagar em {parcela}x de R${(preco + (preco * 20 / 100)) / parcela:.2f} no cartão.')
else:
    print('Erro ao calcular o preço do produto. A opção inserida é inválida.')
