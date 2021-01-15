# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Insira o salário atual do funcionário: R$'))
novosalario = salario + (salario * 15 / 100)

print(f'O salário atual do funcionário é: R${salario:.2f}.')
print(f'Com o aumento de 15%, o funcionário receberá R${novosalario:.2f}.')
