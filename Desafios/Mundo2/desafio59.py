"""Crie um programa que leia DOIS VALORES e mostre um MENU na tela:
[1]SOMAR
[2]MULTIPLICAR
[3]MAIOR
[4]NOVOS NÚMEROS
[5]SAIR DO PROGRAMA
- Seu programa deverá realizar a operação solicitada em cada caso."""

from time import sleep
# COM O BREAK APÓS CADA OPÇÃO:

'''numeros = 1

while numeros != 0:
    num1 = int(input('Digite um número inteiro: '))
    num2 = int(input('Digite outro número inteiro: '))
    numeros = num1, num2
    print(':::' * 15)
    opcao = int(input('Escolha o que deseja fazer com esses números:\n'
                      '[ 1 ] SOMAR\n'
                      '[ 2 ] MULTIPLICAR\n'
                      '[ 3 ] MAIOR\n'
                      '[ 4 ] NOVOS NÚMEROS\n'
                      '[ 5 ] SAIR DO PROGRAMA\n'
                      '- Digite a opção desejada: '))
    if opcao == 1:
        print(f' - A soma dos dois valores digitados é: {num1 + num2}.')
        break
    if opcao == 2:
        print(f'- O resultado da multiplicação dos dois valores é: {num1 * num2}.')
        break
    if opcao == 3:
        print(f'-O maior número inserido foi: {max(numeros)}')
        break
    if opcao == 4:
        print('-Você optou por escolher outros números.')
    if opcao == 5:
        print('- Você optou por finalizar o programa.')
        break'''

# SEM O BREAK NAS OPÇÕES, POSSIBILITANDO O PROGRAMA FAZER OUTRAS ESCOLHAS:
numeros = 1

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
while numeros != 0:
    numeros = num1, num2
    print(':::' * 20)
    sleep(0.5)
    opcao = int(input('Escolha uma opção\n'
                      '[ 1 ] SOMAR\n'
                      '[ 2 ] MULTIPLICAR\n'
                      '[ 3 ] MAIOR\n'
                      '[ 4 ] NOVOS NÚMEROS\n'
                      '[ 5 ] SAIR DO PROGRAMA\n'
                      '- Digite a opção desejada: '))
    if opcao == 1:
        sleep(0.5)
        print(f' - A soma dos dois valores digitados é: {num1} + {num2} = {num1 + num2}.')
    if opcao == 2:
        sleep(0.5)
        print(f'- O resultado da multiplicação dos dois valores é: {num1} x {num2} = {num1 * num2}.')
    if opcao == 3:
        sleep(0.5)
        print(f'-O maior número inserido foi: {max(numeros)}')
    if opcao == 4:
        print(':::' * 20)
        print('-Você optou por escolher outros números.')
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
        sleep(0.5)
    if opcao == 5:
        sleep(0.5)
        print('- Você optou por finalizar o programa.')
        break
    if opcao > 5:
        print('ESCOLHA INVÁLIDA, TENTE NOVAMENTE!')
