"""Crie um programa que leia DOIS VALORES e mostre um MENU na tela:
[1]SOMAR
[2]MULTIPLICAR
[3]MAIOR
[4]NOVOS NÚMEROS
[5]SAIR DO PROGRAMA
- Seu programa deverá realizar a operação solicitada em cada caso."""

numeros = 1

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
        break
    # print(numeros)
