# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
# tabela abaixo:
# - Abaixo de 18.5: ABAIXO DO PESO.
# - Entre 18.5 e 25: PESO IDEAL.
# - 25 até 30: SOBREPESO.
# - 30 até 40: OBESIDADE.
# - Acima de 40: OBESIDADE MÓRBIDA.

peso = float(input('\033[7mInsira seu peso (Kg):\033[m '))
altura = float(input('\033[7mInsira sua altura em metros:\033[m '))
imc = peso / (altura ** 2)
# print(imc)

if imc <= 18.5:
    print(f'Seu \033[1mÍndice de Massa Corporal\033[m é de \033[1;35m{imc:.1f}\033[m. '
          f'Você está \033[1;33mABAIXO DO PESO\033[m.')
elif imc <= 25:
    print(f'Seu \033[1mÍndice de Massa Corporal\033[m é de \033[1;35m{imc:.1f}\033[m. '
          f'Você está com o \033[1;32mPESO IDEAL\033[m.')
elif imc <= 30:
    print(f'Seu \033[1mÍndice de Massa Corporal\033[m é de \033[1;35m{imc:.1f}\033[m. '
          f'Você está com \033[1;33mSOBREPESO\033[m.')
elif imc <= 40:
    print(f'Seu \033[1mÍndice de Massa Corporal\033[m é de \033[1;35m{imc:.1f}\033[m. '
          f'Você está \033[1;31mOBESO(A)\033[m.')
else:
    print(f'Seu \033[1mÍndice de Massa Corporal\033[m é de \033[1;35m{imc:.1f}\033[m. '
          f'Você está com \033[1;31mOBESIDADE MÓRBIDA\033[1;31m.')
