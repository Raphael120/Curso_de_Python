# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# - Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# - Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Insira o valor do seu salário: R$'))
salario10 = salario + (salario * 10) / 100
salario15 = salario + (salario * 15) / 100
# print(salario10) = aumento de 10%
# print(salario15) = aumento de 15%
if salario > 1250:
    print(f'- Seu salário é de R${salario:.2f}. Com um aumento de 10%, seu salário passará a ser de R${salario10:.2f}')
    # ou: novo = salario + (salario * 10 / 100)
else:
    print(f'- Seu salário é de R${salario:.2f}. Com um aumento de 15%, seu salário passará a ser de R${salario15:.2f}')
    # ou: novo = salario + (salario * 15 / 100)
