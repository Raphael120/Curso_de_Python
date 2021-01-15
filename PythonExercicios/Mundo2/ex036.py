# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o 'valor
# da casa', o 'salário' do comprador e em 'quantos anos' ele vai pagar. Calcule o valor da prestação mensal, sabendo que
# ela não pode exceder 30% do salário ou então o empréstimo será negado.

# casa = float(input('Insira o valor da casa a ser comprada: R$'))
# salario = float(input('Insira o valor de seu salário: R$'))
# tempo = int(input('Por quanto tempo você pretende pagar pela casa? '))
# prestacao = casa / (tempo * 12)
#
# print('=' * 120)
# print(f'\033[1;33mA casa custa R${casa:.0f}. Se o banco aprovar o empréstimo,'
#       f' você pagará uma prestação de R${prestacao:.2f} mensais durante {tempo} anos.\033[m')
# print('=' * 120)
#
# if salario * 30 / 100 <= prestacao:
#     print('\033[1;31mEmpréstimo NEGADO.\033[m')
# else:
#     print('\033[1;32mEmpréstimo APROVADO.\033[m')

casa = float(input('Insira o valor da casa a ser comprada: R$'))
salario = float(input('Insira o valor de seu salário: R$'))
tempo = int(input('Por quanto tempo você pretende pagar pela casa? '))
prestacao = casa / (tempo * 12)

print('=' * 120)
print(f'A casa custa R${casa:.0f}. Se o banco aprovar o empréstimo, você pagará uma prestação de R${prestacao:.2f} mensais durante {tempo} anos.')
print('=' * 120)

if salario * 30 / 100 <= prestacao:
    print('Empréstimo NEGADO.')
else:
    print('Empréstimo APROVADO.')
